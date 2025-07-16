import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, ttk
import socket
import json
import threading
import os

__version__ = "0.0.0"
__author__ = "Teeraphat Kullanankanjana"

CYBERPI_PORT_DEFAULT = 12345

def log_message(message, tag="info"):
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

def populate_treeview(tree_dict, parent=''):
    file_tree.delete(*file_tree.get_children())
    def _populate(node_dict, parent_id):
        for key, val in node_dict.items():
            if val is None:
                file_tree.insert(parent_id, 'end', text=key, open=True, tags=('file',))
            else:
                node_id = file_tree.insert(parent_id, 'end', text=key, open=True, tags=('folder',))
                _populate(val, node_id)
    _populate(tree_dict, parent)

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
    port = int(port_entry.get().strip())
    if not ip:
        messagebox.showwarning("Warning", "Please enter CyberPi IP address.")
        log_message("Please enter CyberPi IP address.", tag="warn")
        return
    log_message("[CyberPi] Connecting to {}:{} ...".format(ip, port), tag="connecting")

    def worker():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((ip, port))
            sock.sendall(b"LIST_FILES")
            data = b''
            while True:
                part = sock.recv(4096)
                if not part:
                    break
                data += part
            sock.close()
            files = json.loads(data.decode())
            log_message("[CyberPi] {} files listed.".format(len(files)), tag="files_listed")
            tree_dict = paths_to_tree(files)
            populate_treeview(tree_dict)
            notebook.select(tab_file_manager)
        except Exception as e:
            log_message("[Error] Error connecting to CyberPi: {}".format(e), tag="error")
            messagebox.showerror("Error", "Failed to connect or get files:\n{}".format(e))

    threading.Thread(target=worker, daemon=True).start()

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("Python or MP3 files", "*.py *.mp3")])
    if filepath:
        if not filepath.lower().endswith(('.py', '.mp3')):
            log_message("[Error] Only .py and .mp3 files are allowed.", tag="error")
            return
        file_path_entry.config(state='normal')
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, filepath)
        file_path_entry.config(state='disabled')
        log_message("[Info] Selected file: {}".format(filepath))
    else:
        log_message("[Warning] File selection cancelled.", tag="warn")

def clear_fields():
    ip_entry.delete(0, 'end')
    port_entry.delete(0, 'end')
    port_entry.insert(0, str(CYBERPI_PORT_DEFAULT))
    file_path_entry.config(state='normal')
    file_path_entry.delete(0, 'end')
    file_path_entry.config(state='disabled')
    upload_to_entry.config(state='normal')
    upload_to_entry.delete(0, 'end')
    upload_to_entry.config(state='disabled')
    log_message("[Info] Cleared IP, port, and file path fields.")

def rename_file():
    selected = file_tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a file or folder to rename.")
        return
    old_name = file_tree.item(selected, 'text')
    old_path = get_full_path(selected)
    new_name = simpledialog.askstring("Rename", "Enter new name:", initialvalue=old_name)
    if not new_name:
        return

    def worker():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip_entry.get().strip(), int(port_entry.get().strip())))
            cmd = "RENAME|{}|{}".format(old_path, new_name)
            sock.sendall(cmd.encode())
            response = sock.recv(1024).decode()
            log_message("[Info] Rename response: {}".format(response))
            sock.close()
            if response.startswith("OK"):
                connect_and_list_files()
        except Exception as e:
            log_message("[Error] Error renaming: {}".format(e), tag="error")

    threading.Thread(target=worker, daemon=True).start()

def delete_file():
    selected = file_tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a file or folder to delete.")
        return
    name = file_tree.item(selected, 'text')
    if not messagebox.askyesno("Delete", "Delete '{}'?".format(name)):
        return
    path = get_full_path(selected)

    def worker():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip_entry.get().strip(), int(port_entry.get().strip())))
            cmd = "DELETE|{}".format(path)
            sock.sendall(cmd.encode())
            response = sock.recv(1024).decode()
            log_message("[Info] Delete response: {}".format(response))
            sock.close()
            if response.startswith("OK"):
                connect_and_list_files()
        except Exception as e:
            log_message("[Error] Error deleting: {}".format(e), tag="error")

    threading.Thread(target=worker, daemon=True).start()

def upload_file():
    filepath = file_path_entry.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please select a file to upload.")
        return
    if not os.path.isfile(filepath):
        messagebox.showwarning("Warning", "Selected file does not exist.")
        return

    target_dir = upload_to_entry.get().rstrip('/')
    filename = os.path.basename(filepath)
    target_path = "{}/{}".format(target_dir, filename) if target_dir else "/{}".format(filename)

    def worker():
        try:
            filesize = os.path.getsize(filepath)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip_entry.get().strip(), int(port_entry.get().strip())))
            cmd = "UPLOAD|{}|{}".format(target_path, filesize)
            sock.sendall(cmd.encode())

            ack = sock.recv(1024).decode()
            if not ack.startswith("OK"):
                log_message("[Error] Upload error: {}".format(ack), tag="error")
                sock.close()
                return

            with open(filepath, 'rb') as f:
                while True:
                    chunk = f.read(1024)
                    if not chunk:
                        break
                    sock.sendall(chunk)
            response = sock.recv(1024).decode()
            tag = "uploaded_ok" if response.startswith("OK") else "error"
            log_message("[Warning] Upload response: {}".format(response), tag=tag)
            sock.close()
            if response.startswith("OK"):
                connect_and_list_files()
        except Exception as e:
            log_message("[Error] Error uploading: {}".format(e), tag="error")

    threading.Thread(target=worker, daemon=True).start()

def download_file():
    selected = file_tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a file to download.")
        return
    if file_tree.get_children(selected):
        messagebox.showwarning("Warning", "Cannot download a folder. Please select a file.")
        return

    remote_path = get_full_path(selected)
    ip = ip_entry.get().strip()
    port = int(port_entry.get().strip())
    if not ip:
        messagebox.showwarning("Warning", "Please enter CyberPi IP address.")
        return

    filename = os.path.basename(remote_path)
    save_path = filedialog.asksaveasfilename(
        title="Save Downloaded File As",
        initialfile=filename,
        defaultextension=".py",
        filetypes=[("All Files", "*.*")]
    )
    if not save_path:
        log_message("[Warning] Download cancelled.", tag="warn")
        return

    log_message("[CyberPi] Downloading file {} ...".format(remote_path), tag="connecting")

    def worker():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(15)
            sock.connect((ip, port))
            cmd = "DOWNLOAD|{}".format(remote_path)
            sock.sendall(cmd.encode())

            header = sock.recv(1024).decode()
            if not header.startswith("SIZE|"):
                log_message("[Error] Unexpected response: {}".format(header), tag="error")
                sock.close()
                return
            filesize = int(header.split("|")[1])
            sock.sendall(b"OK")

            with open(save_path, 'wb') as f:
                received = 0
                while received < filesize:
                    chunk = sock.recv(1024)
                    if not chunk:
                        break
                    f.write(chunk)
                    received += len(chunk)
            sock.close()
            log_message("[Info] Downloaded and saved to: {}".format(save_path), tag="uploaded_ok")
        except Exception as e:
            log_message("[Error] Download failed: {}".format(e), tag="error")

    threading.Thread(target=worker, daemon=True).start()

def on_tree_left_click(event):
    item_id = file_tree.identify_row(event.y)
    if not item_id:
        return
    if file_tree.item(item_id, 'text') == "CyberPi":
        return

    upload_to_entry.config(state='normal')
    if file_tree.get_children(item_id):  # โฟลเดอร์
        full_path = get_full_path(item_id)
    else:  # ไฟล์
        full_path = get_full_path(item_id)  # full path ไฟล์เลย
    upload_to_entry.delete(0, tk.END)
    upload_to_entry.insert(0, full_path)
    upload_to_entry.config(state='disabled')

def on_tree_right_click(event):
    item_id = file_tree.identify_row(event.y)
    if not item_id:
        return
    file_tree.selection_set(item_id)
    popup_menu.post(event.x_root, event.y_root)

# --- GUI Layout ---
app = tk.Tk()
app.title("CyberPi File Manager - Version " + __version__)
app.geometry("800x600")

popup_menu = tk.Menu(app, tearoff=0)
popup_menu.add_command(label="Download", command=download_file)
popup_menu.add_command(label="Rename", command=rename_file)
popup_menu.add_command(label="Delete", command=delete_file)

notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill='both', pady=(0, 60))

tab_getting_started = ttk.Frame(notebook)
tab_file_manager = ttk.Frame(notebook)
notebook.add(tab_getting_started, text="Getting Started")
notebook.add(tab_file_manager, text="File Manager")

# Tab 1
frame_ip = tk.Frame(tab_getting_started)
frame_ip.pack(pady=20)

tk.Label(frame_ip, text="CyberPi IP", font=("Arial", 14)).pack(side='left', padx=5)
ip_entry = tk.Entry(frame_ip, width=20, font=("Arial", 14), fg="red")
ip_entry.pack(side='left', padx=5)

tk.Label(frame_ip, text="Port", font=("Arial", 14)).pack(side='left', padx=5)
port_entry = tk.Entry(frame_ip, width=6, font=("Arial", 14), fg="blue")
port_entry.pack(side='left', padx=5)
port_entry.insert(0, str(CYBERPI_PORT_DEFAULT))

tk.Button(frame_ip, text="Connect", font=("Arial", 14), command=connect_and_list_files).pack(side='left', padx=5)

# Tab 2
frame_upload_file = tk.Frame(tab_file_manager)
frame_upload_file.pack(pady=(10, 5), anchor='w')

tk.Label(frame_upload_file, text="File Path", font=("Arial", 12)).pack(side='left')
file_path_entry = tk.Entry(frame_upload_file, width=40, font=("Arial", 12), fg="blue", state='disabled')
file_path_entry.pack(side='left', padx=5)

tk.Button(frame_upload_file, text="Browse", font=("Arial", 12), command=browse_file).pack(side='left', padx=5)
tk.Button(frame_upload_file, text="Clear", font=("Arial", 12), command=clear_fields).pack(side='left', padx=5)

frame_upload_target = tk.Frame(tab_file_manager)
frame_upload_target.pack(pady=(0, 10), anchor='w')

tk.Label(frame_upload_target, text="Upload To", font=("Arial", 12)).pack(side='left', padx=5)
upload_to_entry = tk.Entry(frame_upload_target, width=30, font=("Arial", 12), fg="black", state='disabled')
upload_to_entry.pack(side='left', padx=5)

tk.Button(frame_upload_target, text="Upload File", font=("Arial", 12), command=upload_file).pack(side='left', padx=10)

file_tree = ttk.Treeview(tab_file_manager)
file_tree.pack(fill='both', expand=True, padx=10, pady=10)
file_tree.tag_configure('folder', foreground='purple', font=('Arial', 10, 'bold'))
file_tree.tag_configure('file', foreground='blue', font=('Arial', 10, 'italic'))

file_tree.bind("<Button-1>", on_tree_left_click)
file_tree.bind("<Button-3>", on_tree_right_click)

console_frame = tk.Frame(app)
console_frame.pack(side='bottom', fill='both', padx=5, pady=5)

console_text = tk.Text(console_frame, height=7, font=("Consolas", 10), bg="black", fg="green", state='disabled', wrap='none')
console_text.pack(side='left', fill='both', expand=True)

scrollbar_y = tk.Scrollbar(console_frame, orient='vertical', command=console_text.yview)
scrollbar_y.pack(side='right', fill='y')
console_text.config(yscrollcommand=scrollbar_y.set)

scrollbar_x = tk.Scrollbar(app, orient='horizontal', command=console_text.xview)
scrollbar_x.pack(side='bottom', fill='x')
console_text.config(xscrollcommand=scrollbar_x.set)

btn_frame = tk.Frame(app)
btn_frame.pack(side='bottom', fill='x', padx=5, pady=(0, 10))

tk.Button(btn_frame, text="Copy Console", command=copy_console).pack(side='left', padx=5)
tk.Button(btn_frame, text="Clear Console", command=clear_console).pack(side='left', padx=5)

console_text.tag_config("info", foreground="green")
console_text.tag_config("error", foreground="red")
console_text.tag_config("warn", foreground="orange")
console_text.tag_config("cyberpi", foreground="purple")
console_text.tag_config("welcome", foreground="white")
console_text.tag_config("connecting", foreground="green")
console_text.tag_config("files_listed", foreground="purple")
console_text.tag_config("uploaded_ok", foreground="goldenrod")

log_message("[Welcome] CyberPi File Manager - Version {} by {}".format(__version__, __author__), tag="welcome")

app.mainloop()
