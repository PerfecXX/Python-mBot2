"""
Author      : Teeraphat Kullanankanjana
Version     : 1.0.0
Date        : 2025-07-17
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.
Description : This script provides a graphical user interface (GUI) for managing files
              on a CyberPi device remotely via Wi-Fi. It allows users to list files,
              upload, download, rename, and delete files/folders.
"""

import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, ttk
import socket
import json
import threading
import os

# --- Global Constants ---
CYBERPI_PORT_DEFAULT = 12345 # Default port for CyberPi server

# --- GUI Helper Functions ---
def log_message(message, tag="info"):
    """
    Logs messages to the console text widget in the GUI, with optional tags for styling.
    """
    console_text.config(state='normal') # Enable editing
    console_text.insert(tk.END, message + "\n", tag) # Insert message
    console_text.config(state='disabled') # Disable editing
    console_text.see(tk.END) # Scroll to the end

def copy_console():
    """Copies the content of the console text widget to the clipboard."""
    app.clipboard_clear()
    text = console_text.get('1.0', 'end-1c')
    app.clipboard_append(text)
    log_message("Console copied to clipboard.", tag="info")

def clear_console():
    """Clears the content of the console text widget."""
    console_text.config(state='normal')
    console_text.delete('1.0', tk.END)
    console_text.config(state='disabled')

def paths_to_tree(file_list_dicts):
    """
    Converts a list of file/folder dictionaries (from CyberPi) into a nested dictionary
    structure suitable for populating a Treeview widget.
    """
    tree = {}
    for item in file_list_dicts:
        path = item["path"]
        item_type = item["type"]

        parts = path.strip('/').split('/') # Split path into components
        current = tree
        for i, part in enumerate(parts):
            if part == '': # Skip empty parts from leading/trailing slashes
                continue
            
            if i == len(parts) - 1: # This is the last part of the path (file or folder name)
                if item_type == "dir":
                    # If it's a directory, ensure it's represented as a dictionary
                    if part not in current or current[part] is None:
                        current[part] = {} 
                    current = current[part] # Move into the newly created/existing directory
                else: # It's a file
                    current.setdefault(part, None) # Mark as a leaf node (file)
            else: # This is an intermediate directory
                if part not in current or current[part] is None:
                    current[part] = {}
                current = current[part]
    return {"CyberPi": tree} # Wrap in a root "CyberPi" node

def populate_treeview(tree_dict, parent=''):
    """
    Recursively populates the Tkinter Treeview widget from a nested dictionary structure.
    Assigns 'file' or 'folder' tags for visual styling and identification.
    """
    file_tree.delete(*file_tree.get_children()) # Clear existing items
    def _populate(node_dict, parent_id):
        for key, val in node_dict.items():
            if val is None: # If value is None, it's a file
                file_tree.insert(parent_id, 'end', text=key, open=True, tags=('file',))
            else: # If value is a dictionary, it's a folder
                node_id = file_tree.insert(parent_id, 'end', text=key, open=True, tags=('folder',))
                _populate(val, node_id) # Recurse for subfolders
    _populate(tree_dict, parent)

def get_full_path(item_id):
    """
    Constructs the full absolute path of a selected item in the Treeview.
    """
    parts = []
    while item_id:
        parts.insert(0, file_tree.item(item_id, 'text')) # Get item text (name)
        item_id = file_tree.parent(item_id) # Get parent item
    if parts and parts[0] == "CyberPi": # Remove the virtual root node
        parts.pop(0)
    
    if not parts: # If nothing is left, it's the root directory
        return "/"
        
    return '/' + '/'.join(parts) # Join parts with slashes and add leading slash

# --- Core Client Logic Functions ---
def connect_and_list_files():
    """
    Connects to the CyberPi server, sends a LIST_FILES command,
    and populates the Treeview with the received file list.
    Handles connection errors and JSON parsing.
    """
    ip = ip_entry.get().strip()
    port = int(port_entry.get().strip())
    if not ip:
        messagebox.showwarning("Warning", "Please enter CyberPi IP address.")
        log_message("Please enter CyberPi IP address.", tag="warn")
        return
    log_message("[CyberPi] Connecting to {}:{} ...".format(ip, port), tag="connecting")

    def worker():
        """Worker thread for network operations to prevent GUI freezing."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10) # Set a timeout for connection and initial response
            sock.connect((ip, port))
            sock.sendall(b"LIST_FILES") # Send the command

            # Receive all data until connection closes or no more data
            data = b''
            while True:
                part = sock.recv(4096)
                if not part:
                    break
                data += part
            sock.close()
            
            if not data:
                raise ValueError("Received empty response from CyberPi.")

            # Parse the JSON data (list of dictionaries)
            files_info = json.loads(data.decode())
            
            # Convert the flat list to a nested tree structure for the Treeview
            tree_dict = paths_to_tree(files_info) 

            log_message("[CyberPi] {} files and folders listed.".format(len(files_info)), tag="files_listed")
            populate_treeview(tree_dict) # Populate the Treeview
            notebook.select(tab_file_manager) # Switch to File Manager tab
        except ConnectionRefusedError:
            log_message("[Error] Connection refused by CyberPi at {}:{}. Is the server running?".format(ip, port), tag="error")
            messagebox.showerror("Connection Error", "Connection refused. Please ensure CyberPi server is running at {}:{}".format(ip, port))
        except socket.timeout:
            log_message("[Error] Connection to CyberPi timed out at {}:{}. Check IP/Port or network.".format(ip, port), tag="error")
            messagebox.showerror("Connection Timeout", "Connection to CyberPi timed out. Check IP/Port or network connectivity.")
        except json.JSONDecodeError as e:
            log_message("[Error] Failed to decode JSON from CyberPi: {}. Raw data: {}...".format(e, data.decode(errors='ignore')[:200]), tag="error")
            messagebox.showerror("JSON Decode Error", "Failed to read file list from CyberPi. Raw data might be corrupted or empty.")
        except Exception as e:
            log_message("[Error] Error connecting to CyberPi: {}".format(e), tag="error")
            messagebox.showerror("Error", "Failed to connect or get files:\n{}".format(e))

    threading.Thread(target=worker, daemon=True).start() # Run network operation in a separate thread

def browse_file():
    """
    Opens a file dialog to allow the user to select a local file for upload.
    Updates the local file path entry and automatically suggests an upload target.
    """
    # Allow all file types to be selected
    filepath = filedialog.askopenfilename(filetypes=[("All Files", "*.*"), ("Python Files", "*.py"), ("MP3 Files", "*.mp3"), ("Image Files", "*.jpg *.jpeg *.png"), ("Binary Files", "*.bin")])
    if filepath:
        file_path_entry.config(state='normal')
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, filepath)
        file_path_entry.config(state='disabled')
        log_message("[Info] Selected local file: {}".format(filepath))

        # Automatically suggest an 'Upload To' path based on current Treeview selection
        selected = file_tree.focus()
        if not selected or file_tree.item(selected, 'text') == "CyberPi":
            # If no item or root "CyberPi" is selected, default to root directory
            target_path_for_upload = "/"
        else:
            full_remote_path = get_full_path(selected)
            if file_tree.tag_has('folder', selected):
                # If a folder is selected, upload into that folder
                target_path_for_upload = full_remote_path
                if not target_path_for_upload.endswith('/'):
                    target_path_for_upload += '/' # Ensure it's treated as a directory
            else: # A file is selected
                # If a file is selected, upload into its parent directory (default behavior for many clients)
                target_path_for_upload = os.path.dirname(full_remote_path)
                if not target_path_for_upload.endswith('/'):
                    target_path_for_upload += '/'
                if not target_path_for_upload: # Handle case like '/file.py' whose dirname is '/'
                    target_path_for_upload = '/'
        
        upload_to_entry.config(state='normal')
        upload_to_entry.delete(0, tk.END)
        upload_to_entry.insert(0, target_path_for_upload)
        upload_to_entry.config(state='disabled')

    else:
        log_message("[Warning] File selection cancelled.", tag="warn")

def clear_fields():
    """Clears the input fields for IP, Port, Local File Path, and Upload To."""
    ip_entry.delete(0, 'end')
    port_entry.delete(0, 'end')
    port_entry.insert(0, str(CYBERPI_PORT_DEFAULT))
    
    file_path_entry.config(state='normal')
    file_path_entry.delete(0, 'end')
    file_path_entry.config(state='disabled')
    
    upload_to_entry.config(state='normal')
    upload_to_entry.delete(0, 'end')
    upload_to_entry.insert(0, "/") # Reset to root
    upload_to_entry.config(state='disabled')
    
    log_message("[Info] Cleared IP, port, and file path fields.")

def rename_file():
    """
    Renames a selected file or folder on the CyberPi.
    Prompts the user for a new name and sends a RENAME command to the server.
    """
    selected = file_tree.focus()
    if not selected or file_tree.item(selected, 'text') == "CyberPi":
        messagebox.showwarning("Warning", "Please select a file or folder to rename (not the root).")
        log_message("[Warn] No valid item selected for rename.", tag="warn")
        return
    old_name = file_tree.item(selected, 'text')
    old_path = get_full_path(selected)
    new_name = simpledialog.askstring("Rename", "Enter new name:", initialvalue=old_name)
    if not new_name or new_name.strip() == "":
        log_message("[Info] Rename cancelled or empty new name provided.", tag="info")
        return

    if '/' in new_name or '\\' in new_name:
        messagebox.showwarning("Invalid Name", "New name cannot contain '/' or '\\' characters.")
        log_message("[Warn] Invalid characters in new name for rename.", tag="warn")
        return

    log_message("[CyberPi] Renaming '{}' to '{}' ...".format(old_path, new_name), tag="info")
    def worker():
        """Worker thread for rename operation."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((ip_entry.get().strip(), int(port_entry.get().strip())))
            cmd = "RENAME|{}|{}".format(old_path, new_name)
            sock.sendall(cmd.encode())
            response = sock.recv(1024).decode() # Get server response
            log_message("[Info] Rename response: {}".format(response))
            sock.close()
            if response.startswith("OK"):
                connect_and_list_files() # Refresh file list after successful rename
                log_message("[CyberPi] Successfully renamed to '{}'.".format(new_name), tag="uploaded_ok")
            else:
                messagebox.showerror("Rename Error", "Failed to rename:\n{}".format(response))
                log_message("[Error] Rename failed: {}".format(response), tag="error")
        except Exception as e:
            log_message("[Error] Error during rename operation: {}".format(e), tag="error")
            messagebox.showerror("Error", "Failed to connect or rename:\n{}".format(e))

    threading.Thread(target=worker, daemon=True).start()

def delete_file():
    """
    Deletes a selected file or folder on the CyberPi.
    Asks for user confirmation and sends a DELETE command to the server.
    """
    selected = file_tree.focus()
    if not selected or file_tree.item(selected, 'text') == "CyberPi":
        messagebox.showwarning("Warning", "Please select a file or folder to delete (not the root).")
        log_message("[Warn] No valid item selected for delete.", tag="warn")
        return
    name = file_tree.item(selected, 'text')
    
    confirm_message = "Are you sure you want to delete '{}'?".format(name)
    if file_tree.tag_has('folder', selected):
        confirm_message = "WARNING: Deleting folder '{}' will delete all its contents. Are you sure?".format(name)

    if not messagebox.askyesno("Delete Confirmation", confirm_message):
        log_message("[Info] Delete cancelled by user.", tag="info")
        return
    
    path = get_full_path(selected)
    log_message("[CyberPi] Deleting '{}' ...".format(path), tag="info")

    def worker():
        """Worker thread for delete operation."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((ip_entry.get().strip(), int(port_entry.get().strip())))
            cmd = "DELETE|{}".format(path)
            sock.sendall(cmd.encode())
            response = sock.recv(1024).decode() # Get server response
            log_message("[Info] Delete response: {}".format(response))
            sock.close()
            if response.startswith("OK"):
                connect_and_list_files() # Refresh file list after successful deletion
                log_message("[CyberPi] Successfully deleted '{}'.".format(path), tag="uploaded_ok")
            else:
                messagebox.showerror("Delete Error", "Failed to delete:\n{}".format(response))
                log_message("[Error] Delete failed: {}".format(response), tag="error")
        except Exception as e:
            log_message("[Error] Error during delete operation: {}".format(e), tag="error")
            messagebox.showerror("Error", "Failed to connect or delete:\n{}".format(e))

    threading.Thread(target=worker, daemon=True).start()

def upload_file():
    """
    Uploads the selected local file to the specified target path on CyberPi.
    Sends UPLOAD command, file size, and then the file data.
    """
    filepath = file_path_entry.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please select a local file to upload first.")
        log_message("[Warn] No local file selected for upload.", tag="warn")
        return
    if not os.path.isfile(filepath):
        messagebox.showwarning("Warning", "Selected file '{}' does not exist locally.".format(filepath))
        log_message("[Error] Local file '{}' not found.".format(filepath), tag="error")
        return

    # The target path on CyberPi (either a folder path or a specific file path to overwrite)
    target_dir_or_file = upload_to_entry.get().strip()
    filename = os.path.basename(filepath)

    # Determine the final target path on CyberPi based on whether the target is a directory or a file
    if target_dir_or_file.endswith('/'): # If target ends with '/', it's a directory
        final_target_path = "{}{}".format(target_dir_or_file, filename) # Append filename
    else: # Otherwise, it's a specific file path to overwrite
        final_target_path = target_dir_or_file
    
    # Ensure the final target path starts with a '/' for absolute path
    if not final_target_path.startswith('/'):
        final_target_path = '/' + final_target_path

    log_message("[CyberPi] Preparing to upload '{}' to '{}' ...".format(filepath, final_target_path), tag="connecting")

    def worker():
        """Worker thread for upload operation."""
        try:
            filesize = os.path.getsize(filepath) # Get local file size
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(60) # Set a longer timeout for large files
            sock.connect((ip_entry.get().strip(), int(port_entry.get().strip())))
            cmd = "UPLOAD|{}|{}".format(final_target_path, filesize) # Send UPLOAD command with target path and size
            sock.sendall(cmd.encode())

            ack = sock.recv(1024).decode() # Wait for server's "OK|Ready"
            if not ack.startswith("OK"):
                log_message("[Error] Upload initiation failed: {}".format(ack), tag="error")
                messagebox.showerror("Upload Error", "CyberPi did not confirm readiness:\n{}".format(ack))
                sock.close()
                return

            # Read local file in chunks and send
            with open(filepath, 'rb') as f:
                sent_bytes = 0
                while True:
                    chunk = f.read(1024) # Read 1KB chunks
                    if not chunk: # End of file
                        break
                    sock.sendall(chunk)
                    sent_bytes += len(chunk)
                    
            response = sock.recv(1024).decode() # Get final response from server
            tag = "uploaded_ok" if response.startswith("OK") else "error"
            log_message("[Info] Upload response: {}".format(response), tag=tag)
            sock.close()
            if response.startswith("OK"):
                connect_and_list_files() # Refresh file list after successful upload
                messagebox.showinfo("Upload Complete", "File '{}' uploaded successfully to CyberPi.".format(filename))
            else:
                messagebox.showerror("Upload Error", "Upload failed on CyberPi:\n{}".format(response))
        except socket.timeout:
            log_message("[Error] Upload timed out for '{}'.".format(filepath), tag="error")
            messagebox.showerror("Upload Timeout", "Upload of '{}' timed out. Check connection or file size.".format(filename))
        except Exception as e:
            log_message("[Error] Error during upload: {}".format(e), tag="error")
            messagebox.showerror("Error", "Failed to connect or upload:\n{}".format(e))

    threading.Thread(target=worker, daemon=True).start()

def download_file():
    """
    Downloads a selected file from the CyberPi to a local path.
    Sends DOWNLOAD command, receives file size, and then file data.
    """
    selected = file_tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a file to download.")
        log_message("[Warn] No item selected for download.", tag="warn")
        return
    if file_tree.tag_has('folder', selected):
        messagebox.showwarning("Warning", "Cannot download a folder. Please select a file.")
        log_message("[Warn] Cannot download a folder.", tag="warn")
        return
    if file_tree.item(selected, 'text') == "CyberPi":
        messagebox.showwarning("Warning", "Cannot download the CyberPi root. Please select a file.")
        log_message("[Warn] Cannot download CyberPi root.", tag="warn")
        return

    remote_path = get_full_path(selected)
    ip = ip_entry.get().strip()
    port = int(port_entry.get().strip())
    if not ip:
        messagebox.showwarning("Warning", "Please enter CyberPi IP address.")
        log_message("[Warn] CyberPi IP address not entered.", tag="warn")
        return

    filename = os.path.basename(remote_path)
    save_path = filedialog.asksaveasfilename(
        title="Save Downloaded File As",
        initialfile=filename,
        filetypes=[("All Files", "*.*"), ("Python Files", "*.py"), ("MP3 Files", "*.mp3"), ("Binary Files", "*.bin")]
    )
    if not save_path:
        log_message("[Warning] Download cancelled by user.", tag="warn")
        return

    log_message("[CyberPi] Downloading file '{}' to '{}' ...".format(remote_path, save_path), tag="connecting")

    def worker():
        """Worker thread for download operation."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(60) # Longer timeout for downloads
            sock.connect((ip, port))
            cmd = "DOWNLOAD|{}".format(remote_path)
            sock.sendall(cmd.encode())

            header = sock.recv(1024).decode() # Receive SIZE header
            if not header.startswith("SIZE|"):
                log_message("[Error] Unexpected response from CyberPi: {}".format(header), tag="error")
                messagebox.showerror("Download Error", "Unexpected response from CyberPi:\n{}".format(header))
                sock.close()
                return
            
            try:
                filesize = int(header.split("|")[1]) # Extract file size
            except (ValueError, IndexError):
                log_message("[Error] Invalid file size in header: {}".format(header), tag="error")
                messagebox.showerror("Download Error", "Invalid file size received from CyberPi.")
                sock.close()
                return

            sock.sendall(b"OK") # Acknowledge receipt of size
            
            # Receive file data in chunks and write to local file
            with open(save_path, 'wb') as f:
                received = 0
                while received < filesize:
                    chunk = sock.recv(4096) # Receive 4KB chunks
                    if not chunk:
                        log_message("[Error] Connection closed prematurely during download.", tag="error")
                        break
                    f.write(chunk)
                    received += len(chunk)

            sock.close()
            if received == filesize:
                log_message("[Info] Downloaded and saved to: {}".format(save_path), tag="uploaded_ok")
                messagebox.showinfo("Download Complete", "File downloaded successfully to:\n{}".format(save_path))
            else:
                log_message("[Error] Partial download: Expected {} bytes, got {} bytes.".format(filesize, received), tag="error")
                messagebox.showwarning("Download Warning", "Download incomplete. Expected {} bytes, got {} bytes.".format(filesize, received))

        except socket.timeout:
            log_message("[Error] Download timed out for '{}'.".format(remote_path), tag="error")
            messagebox.showerror("Download Timeout", "Download of '{}' timed out. Check connection or file size.".format(filename))
        except Exception as e:
            log_message("[Error] Download failed: {}".format(e), tag="error")
            messagebox.showerror("Error", "Download failed:\n{}".format(e))

    threading.Thread(target=worker, daemon=True).start()

# --- Event Handlers ---
def on_tree_left_click(event):
    """
    Handles left-clicks on the file treeview.
    Updates the 'Upload To' entry based on the selected item (file or folder).
    """
    item_id = file_tree.identify_row(event.y)
    if not item_id:
        return
    file_tree.selection_set(item_id) # Visually select the clicked item

    full_path_on_cyberpi = get_full_path(item_id)
    target_path_for_upload = ""

    item_tags = file_tree.item(item_id, 'tags') # Get tags (e.g., 'file', 'folder')
    
    if 'folder' in item_tags:
        # If a folder is clicked, set the upload target to that folder (append file into it)
        target_path_for_upload = full_path_on_cyberpi
        if not target_path_for_upload.endswith('/'):
            target_path_for_upload += '/' # Ensure it looks like a directory path
    elif 'file' in item_tags:
        # If a file is clicked, set the upload target to overwrite that specific file
        target_path_for_upload = full_path_on_cyberpi
    else: # Case for the root "CyberPi" node or un-tagged items
        target_path_for_upload = "/" # Default to root

    # Update the Upload To entry field (enable, update, then disable)
    upload_to_entry.config(state='normal')
    upload_to_entry.delete(0, tk.END)
    upload_to_entry.insert(0, target_path_for_upload)
    upload_to_entry.config(state='disabled')
    log_message("[Info] Upload target set to: {}".format(target_path_for_upload))

def on_tree_right_click(event):
    """
    Handles right-clicks on the file treeview to display a context menu.
    """
    item_id = file_tree.identify_row(event.y)
    if not item_id:
        return
    file_tree.selection_set(item_id) # Select item on right-click
    
    if file_tree.item(item_id, 'text') == "CyberPi": # Don't show menu for the root
        return

    popup_menu.post(event.x_root, event.y_root) # Show the context menu

# --- GUI Setup ---
app = tk.Tk()
app.title("CyberPi File Manager - Version 1.0.0") # Update title
app.geometry("800x650")

# Context menu for right-clicking files/folders
popup_menu = tk.Menu(app, tearoff=0)
popup_menu.add_command(label="Download", command=download_file)
popup_menu.add_command(label="Rename", command=rename_file)
popup_menu.add_command(label="Delete", command=delete_file)

# Notebook widget for tabs
notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill='both', pady=(0, 60))

# "Getting Started" Tab
tab_getting_started = ttk.Frame(notebook)
notebook.add(tab_getting_started, text="Getting Started")

frame_ip = tk.Frame(tab_getting_started)
frame_ip.pack(pady=20)

tk.Label(frame_ip, text="CyberPi IP", font=("Arial", 14)).pack(side='left', padx=5)
ip_entry = tk.Entry(frame_ip, width=20, font=("Arial", 14), fg="red")
ip_entry.pack(side='left', padx=5)

tk.Label(frame_ip, text="Port", font=("Arial", 14)).pack(side='left', padx=5)
port_entry = tk.Entry(frame_ip, width=6, font=("Arial", 14), fg="blue")
port_entry.pack(side='left', padx=5)
port_entry.insert(0, str(CYBERPI_PORT_DEFAULT)) # Set default port

tk.Button(frame_ip, text="Connect", font=("Arial", 14), command=connect_and_list_files).pack(side='left', padx=5)

# "File Manager" Tab
tab_file_manager = ttk.Frame(notebook)
notebook.add(tab_file_manager, text="File Manager")

frame_upload_file = tk.Frame(tab_file_manager)
frame_upload_file.pack(pady=(10, 5), anchor='w', padx=10)

tk.Label(frame_upload_file, text="Local File Path", font=("Arial", 12)).pack(side='left')
file_path_entry = tk.Entry(frame_upload_file, width=40, font=("Arial", 12), fg="blue", state='disabled')
file_path_entry.pack(side='left', padx=5)

tk.Button(frame_upload_file, text="Browse...", font=("Arial", 12), command=browse_file).pack(side='left', padx=5)
tk.Button(frame_upload_file, text="Clear", font=("Arial", 12), command=clear_fields).pack(side='left', padx=5)

frame_upload_target = tk.Frame(tab_file_manager)
frame_upload_target.pack(pady=(0, 10), anchor='w', padx=10)

tk.Label(frame_upload_target, text="Upload To (on CyberPi)", font=("Arial", 12)).pack(side='left', padx=5)
upload_to_entry = tk.Entry(frame_upload_target, width=30, font=("Arial", 12), fg="black", state='disabled')
upload_to_entry.pack(side='left', padx=5)
# Initialize upload_to_entry to '/'
upload_to_entry.config(state='normal')
upload_to_entry.insert(0, "/")
upload_to_entry.config(state='disabled')


tk.Button(frame_upload_target, text="Upload File", font=("Arial", 12), command=upload_file).pack(side='left', padx=10)

# Treeview for displaying remote files/folders
file_tree = ttk.Treeview(tab_file_manager)
file_tree.pack(fill='both', expand=True, padx=10, pady=10)
# Configure tags for visual styling
file_tree.tag_configure('folder', foreground='purple', font=('Arial', 10, 'bold'))
file_tree.tag_configure('file', foreground='blue', font=('Arial', 10, 'italic'))

# Bind event handlers to Treeview
file_tree.bind("<Button-1>", on_tree_left_click) # Left-click
file_tree.bind("<Button-3>", on_tree_right_click) # Right-click

# Console Frame for logging messages
console_frame = tk.Frame(app)
console_frame.pack(side='bottom', fill='both', padx=5, pady=5)

console_text = tk.Text(console_frame, height=7, font=("Consolas", 10), bg="black", fg="green", state='disabled', wrap='none')
console_text.pack(side='left', fill='both', expand=True)

# Scrollbars for console
scrollbar_y = tk.Scrollbar(console_frame, orient='vertical', command=console_text.yview)
scrollbar_y.pack(side='right', fill='y')
console_text.config(yscrollcommand=scrollbar_y.set)

scrollbar_x = tk.Scrollbar(app, orient='horizontal', command=console_text.xview)
scrollbar_x.pack(side='bottom', fill='x')
console_text.config(xscrollcommand=scrollbar_x.set)

# Buttons below the console
btn_frame = tk.Frame(app)
btn_frame.pack(side='bottom', fill='x', padx=5, pady=(0, 10))

tk.Button(btn_frame, text="Copy Console", command=copy_console).pack(side='left', padx=5)
tk.Button(btn_frame, text="Clear Console", command=clear_console).pack(side='left', padx=5)

# Console text tag configurations
console_text.tag_config("info", foreground="green")
console_text.tag_config("error", foreground="red")
console_text.tag_config("warn", foreground="orange")
console_text.tag_config("cyberpi", foreground="purple")
console_text.tag_config("welcome", foreground="white")
console_text.tag_config("connecting", foreground="green")
console_text.tag_config("files_listed", foreground="purple")
console_text.tag_config("uploaded_ok", foreground="goldenrod")

log_message("[Welcome] CyberPi File Manager - Version 1.0.0 by Teeraphat Kullanankanjana", tag="welcome") # Initial welcome message

# --- Run the GUI application ---
if __name__ == "__main__":
    app.mainloop()
