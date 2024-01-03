#YUSUFZAINFAUZAN
import tkinter as tk
from tkinter import Label, Entry, Text, Button, messagebox

class RumahSakitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Rumah Sakit")

        self.label_nama_pasien = Label(root, text='Nama Pasien:')
        self.input_nama_pasien = Entry(root)

        self.label_gejala = Label(root, text='Gejala:')
        self.input_gejala = Text(root, height=4, width=30)

        self.btn_diagnosa = Button(root, text='Diagnosa', command=self.diagnosa_pasien)
        self.output_diagnosa = Label(root, text='Hasil Diagnosa:')

        self.layout_elements()

    def layout_elements(self):
        self.label_nama_pasien.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.input_nama_pasien.grid(row=0, column=1, padx=10, pady=10)

        self.label_gejala.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.input_gejala.grid(row=1, column=1, padx=10, pady=10)

        self.btn_diagnosa.grid(row=2, column=0, columnspan=2, pady=10)
        self.output_diagnosa.grid(row=3, column=0, columnspan=2, pady=10)

    def diagnosa_pasien(self):
        while True:
            # Get data from user input
            nama_pasien = self.input_nama_pasien.get()
            gejala = self.input_gejala.get("1.0", "end-1c")

            # Check if input is empty
            if not nama_pasien or not gejala:
                messagebox.showwarning("Peringatan", "Mohon isi semua kolom.")
                break

            # Simple diagnostic logic
            hasil_diagnosa = self.proses_diagnosa(gejala)

            # Display diagnosis result
            self.output_diagnosa.config(text=f'Hasil Diagnosa untuk {nama_pasien}: {hasil_diagnosa}')

            # Ask user if they want to continue
            answer = messagebox.askyesno("Lanjutkan?", "Apakah Anda ingin melanjutkan diagnosa?")
            if not answer:
                break

            # Clear input fields for the next iteration
            self.input_nama_pasien.delete(0, 'end')
            self.input_gejala.delete("1.0", 'end')

    def proses_diagnosa(self, gejala):
        # Simple diagnostic logic
        if 'demam' in gejala.lower() and 'batuk' in gejala.lower():
            return 'Mungkin Anda terkena flu.'
        else:
            return 'Belum dapat didiagnosa. Silakan konsultasikan dengan dokter.'

if __name__ == "__main__":
    root = tk.Tk()
    app = RumahSakitApp(root)
    root.mainloop()
