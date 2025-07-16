import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, ttk
import socket
import json
import threading
import os

__version__ = "1.8.3"
__author__ = "Teeraphat Kullanankanjana"

CYBERPI_PORT_DEFAULT = 12345

def log_message(message, tag="connecting"):
    console_text.config(state='normal')
    console_text.insert(tk.END, message + "\n", tag)
    console_text.config(state='disabled')
    console_text.see(tk.END)

def copy_console():
    app.clipboard_clear()
    text = console_text.get('1.0', 'end-1c')
    app.clipboard_append(text)
    log_message("Console copied to clipboard.", tag="info")

def clear_console():
    console_text.config(state='normal')
    console_text.delete('1.0', tk.END)
    console_text.config(state='disabled')

def paths_to_tree(paths):
    tree = {}
    for path in paths:
        parts = path.strip('/').split('/')
        current = tree
        for i, part in enumerate(parts):
            if part == '':
                continue
            if i == len(parts) - 1:
                current.setdefault(part, None)
            else:
                if part not in current or current[part] is None:
                    current[part] = {}
                current = current[part]
    return {"CyberPi": tree}

def insert_node(parent, node_name):
    return file_tree.insert(parent, 'end', text=node_name, open=True)

def populate_treeview(tree_dict, parent=''):
    file_tree.delete(*file_tree.get_children())
    def _populate(node_dict, parent_id):
        for key, val in node_dict.items():
            node_id = insert_node(parent_id, key)
            if isinstance(val, dict):
                _populate(val, node_id)
    _populate(tree_dict, parent)
    style_tree_items()

def get_full_path(item_id):
    parts = []
    while item_id:
        parts.insert(0, file_tree.item(item_id, 'text'))
        item_id = file_tree.parent(item_id)
    if parts and parts[0] == "CyberPi":
        parts.pop(0)
    return '/' + '/'.join(parts)

def connect_and_list_files():
    ip = ip_entry.get().strip()
    port = port_entry.get().strip()
    if not ip:
        messagebox.showwarning("Warning", "Please enter CyberPi IP address.")
        log_message("Please enter CyberPi IP address.", tag="error")
        return
    try:
        port_num = int(port)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid port number.")
        log_message("Invalid port number entered.", tag="error")
        return

    log_message(f"Connecting to {ip}:{port_num} ...", tag="connecting")

    def worker():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((ip, port_num))
            log_message(f"Connected to {ip}:{port_num}.", tag="connected")

            sock.sendall(b"LIST_FILES")
            data = b''
            while True:
                part = sock.recv(4096)
                if not part:
                    break
                data += part
            sock.close()

            files = json.loads(data.decode())
            log_message(f"Received {len(files)} files.", tag="files_received")

            tree_dict = paths_to_tree(files)
            populate_treeview(tree_dict)
            notebook.select(tab_file_manager)
        except Exception as e:
            log_message(f"Error connecting to CyberPi: {e}", tag="error")
            messagebox.showerror("Error", f"Failed to connect or get files:\n{e}")

    threading.Thread(target=worker, daemon=True).start()

def browse_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("Python or MP3 files", "*.py *.mp3")]
    )
    if filepath:
        if not filepath.lower().endswith(('.py', '.mp3')):
            log_message("Only .py and .mp3 files are allowed.", tag="error")
            return
        file_path_entry.config(state='normal')
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, filepath)
        file_path_entry.config(state='disabled')
        log_message(f"Selected file: {filepath}", tag="info")
    else:
        log_message("File selection cancelled.", tag="warn")

def clear_fields():
    file_path_entry.config(state='normal')
    file_path_entry.delete(0, 'end')
    file_path_entry.config(state='disabled')
    log_message("Cleared file path field.", tag="info")

def rename_file():
    selected = file_tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a file or folder to rename.")
        return
    old_name = file_tree.item(selected, 'text')
    parent = file_tree.parent(selected)
    if parent:
        parent_path = get_full_path(parent)
        old_path = parent_path + '/' + old_name if parent_path != '' else '/' + old_name
    else:
        old_path = '/' + old_name
    new_name = simpledialog.askstring("Rename", "Enter new name:", initialvalue=old_name)
    if not new_name:
        return

    def worker():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((ip_entry.get().strip(), int(port_entry.get().strip())))
            cmd = f"RENAME|{old_path}|{new_name}"
            sock.sendall(cmd.encode())
            response = sock.recv(1024).decode()
            log_message(f"Rename response: {response}", tag="info")
            sock.close()
            if response.startswith("OK"):
                connect_and_list_files()
        except Exception as e:
            log_message(f"Error renaming: {e}", tag="error")

    threading.Thread(target=worker, daemon=True).start()

def delete_file():
    selected = file_tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a file or folder to delete.")
        return
    name = file_tree.item(selected, 'text')
    if not messagebox.askyesno("Delete", f"Delete '{name}'?"):
        return

    parent = file_tree.parent(selected)
    if parent:
        parent_path = get_full_path(parent)
        path = parent_path + '/' + name if parent_path != '' else '/' + name
    else:
        path = '/' + name

    def worker():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((ip_entry.get().strip(), int(port_entry.get().strip())))
            cmd = f"DELETE|{path}"
            sock.sendall(cmd.encode())
            response = sock.recv(1024).decode()
            log_message(f"Delete response: {response}", tag="info")
            sock.close()
            if response.startswith("OK"):
                connect_and_list_files()
        except Exception as e:
            log_message(f"Error deleting: {e}", tag="error")

    threading.Thread(target=worker, daemon=True).start()

def upload_file():
    filepath = file_path_entry.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please select a file to upload.")
        return
    if not os.path.isfile(filepath):
        messagebox.showwarning("Warning", "Selected file does not exist.")
        return

    target_path = upload_to_entry.get().strip()
    if not target_path:
        messagebox.showwarning("Warning", "Upload target path is empty.")
        return

    def worker():
        try:
            filesize = os.path.getsize(filepath)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((ip_entry.get().strip(), int(port_entry.get().strip())))
            cmd = f"UPLOAD|{target_path}|{filesize}"
            sock.sendall(cmd.encode())

            ack = sock.recv(1024).decode()
            if not ack.startswith("OK"):
                log_message(f"Upload error: {ack}", tag="error")
                sock.close()
                return

            with open(filepath, 'rb') as f:
                while True:
                    chunk = f.read(1024)
                    if not chunk:
                        break
                    sock.sendall(chunk)
            response = sock.recv(1024).decode()
            log_message(f"Upload response: {response}", tag="upload_ok")
            sock.close()
            if response.startswith("OK"):
                connect_and_list_files()
        except Exception as e:
            log_message(f"Error uploading: {e}", tag="error")

    threading.Thread(target=worker, daemon=True).start()

def on_tree_left_click(event):
    item_id = file_tree.identify_row(event.y)
    if not item_id:
        return
    if file_tree.item(item_id, 'text') == "CyberPi":
        return
    if not file_tree.get_children(item_id):  # ไฟล์
        full_path = get_full_path(item_id)
        upload_to_entry.config(state='normal')
        upload_to_entry.delete(0, tk.END)
        upload_to_entry.insert(0, full_path)
        upload_to_entry.config(state='disabled')
        # ไม่เซ็ต file_path_entry เพื่อแยกกันชัดเจน

def on_tree_right_click(event):
    item_id = file_tree.identify_row(event.y)
    if not item_id:
        return
    file_tree.selection_set(item_id)
    popup_menu.post(event.x_root, event.y_root)

def style_tree_items():
    for item in file_tree.get_children():
        _style_recursive(item)

def _style_recursive(item):
    children = file_tree.get_children(item)
    if children:
        file_tree.item(item, tags=("folder",))
        for child in children:
            _style_recursive(child)
    else:
        file_tree.item(item, tags=("file",))

# === Main window ===
app = tk.Tk()
app.title("CyberPi File Manager - Version " + __version__)
app.geometry("800x600")
app.resizable(True, True)

# Popup menu for rename/delete
popup_menu = tk.Menu(app, tearoff=0)
popup_menu.add_command(label="Rename", command=rename_file)
popup_menu.add_command(label="Delete", command=delete_file)

notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill='both', pady=(0, 60))

# Tab 1 - Getting Started
tab_getting_started = ttk.Frame(notebook)
notebook.add(tab_getting_started, text="Getting Started")

frame_ip_port = tk.Frame(tab_getting_started)
frame_ip_port.pack(pady=20)

tk.Label(frame_ip_port, text="CyberPi IP", font=("Arial", 14)).pack(side='left', padx=5)
ip_entry = tk.Entry(frame_ip_port, width=20, font=("Arial", 14), fg="red")
ip_entry.pack(side='left', padx=5)

tk.Label(frame_ip_port, text="Port", font=("Arial", 14)).pack(side='left', padx=5)
port_entry = tk.Entry(frame_ip_port, width=8, font=("Arial", 14), fg="blue")
port_entry.insert(0, str(CYBERPI_PORT_DEFAULT))
port_entry.pack(side='left', padx=5)

tk.Button(frame_ip_port, text="Connect", font=("Arial", 14), command=connect_and_list_files).pack(side='left', padx=5)

# Tab 2 - File Manager
tab_file_manager = ttk.Frame(notebook)
notebook.add(tab_file_manager, text="File Manager")

frame_upload = tk.Frame(tab_file_manager)
frame_upload.pack(pady=10, anchor='w')

tk.Label(frame_upload, text="File Path", font=("Arial", 12)).pack(side='left')
file_path_entry = tk.Entry(frame_upload, width=40, font=("Arial", 12), fg="blue", state='disabled')
file_path_entry.pack(side='left', padx=5)

btn_browse_file = tk.Button(frame_upload, text="Browse File", font=("Arial", 12), command=browse_file)
btn_browse_file.pack(side='left', padx=5)

btn_clear_file_path = tk.Button(frame_upload, text="Clear", font=("Arial", 12), command=clear_fields)
btn_clear_file_path.pack(side='left', padx=5)

frame_upload_to = tk.Frame(tab_file_manager)
frame_upload_to.pack(pady=10, anchor='w')

tk.Label(frame_upload_to, text="Upload To", font=("Arial", 12)).pack(side='left')
upload_to_entry = tk.Entry(frame_upload_to, width=40, font=("Arial", 12), fg="purple", state='disabled')
upload_to_entry.pack(side='left', padx=5)

btn_upload = tk.Button(frame_upload_to, text="Upload File", font=("Arial", 12), command=upload_file)
btn_upload.pack(side='left', padx=10)

file_tree = ttk.Treeview(tab_file_manager)
file_tree.pack(fill='both', expand=True, padx=10, pady=10)

file_tree.tag_configure("folder", foreground="purple", font=("Arial", 10, "bold"))
file_tree.tag_configure("file", foreground="blue", font=("Arial", 10, "italic"))

file_tree.bind("<Button-1>", on_tree_left_click)
file_tree.bind("<Button-3>", on_tree_right_click)

# Console frame with scrollbars
console_frame = tk.Frame(app)
console_frame.pack(side='bottom', fill='both', expand=False, padx=5, pady=5)

console_text = tk.Text(console_frame, height=7, font=("Consolas", 10), bg="black", fg="green", state='disabled', wrap='none')
console_text.pack(side='left', fill='both', expand=True)

scrollbar_y = tk.Scrollbar(console_frame, orient='vertical', command=console_text.yview)
scrollbar_y.pack(side='right', fill='y')
console_text.config(yscrollcommand=scrollbar_y.set)

scrollbar_x = tk.Scrollbar(app, orient='horizontal', command=console_text.xview)
scrollbar_x.pack(side='bottom', fill='x')
console_text.config(xscrollcommand=scrollbar_x.set)

# Buttons for Copy and Clear Console (bottom bar)
btn_frame = tk.Frame(app)
btn_frame.pack(side='bottom', fill='x', padx=5, pady=(0,10))

btn_copy_console = tk.Button(btn_frame, text="Copy Console", command=copy_console)
btn_copy_console.pack(side='left', padx=5)

btn_clear_console = tk.Button(btn_frame, text="Clear Console", command=clear_console)
btn_clear_console.pack(side='left', padx=5)

# Configure console text tags for colors
console_text.tag_config("connecting", foreground="#32CD32")    # Green - connecting
console_text.tag_config("connected", foreground="#32CD32")     # Green - connected
console_text.tag_config("files_received", foreground="#8A2BE2") # Purple - files received
console_text.tag_config("upload_ok", foreground="#DAA520")     # Gold - upload ok
console_text.tag_config("error", foreground="#FF4500")         # Red - error
console_text.tag_config("info", foreground="white")            # White - general info
console_text.tag_config("warn", foreground="#DAA520")          # Gold-ish warning

log_message(f"[Welcome] CyberPi File Manager - Version {__version__} by {__author__}", tag="info")

app.mainloop()
