import PyPDF2
from tkinter import filedialog as fd
from tkinter import Tk
from tkinter.messagebox import showinfo

root = Tk()
root.withdraw()
root.attributes('-topmost', True)


def get_pdfs():
    pdf_list = []
    while True:
        # Ask user for pdf files to merge
        answer = input('To select file type (Y) or press Enter to Continue: ')
        if answer.lower() == 'y':
            filename = fd.askopenfilenames(defaultextension='.pdf',
                                           filetypes=[("All Files", "*.*"), ("PDF Documents", "*.pdf")])

            if len(filename):
                for f in filename:
                    pdf_list.append(f)
            else:
                print("Please select a file")
            continue
        else:
            break
    return pdf_list


def save_file():
    combined_pdf = fd.asksaveasfile(initialfile='Untitled.pdf', defaultextension=".pdf",
                                    filetypes=[("All Files", "*.*"), ("PDF Documents", "*.pdf")])
    return combined_pdf


def pdf_combiner():
    pdflist = get_pdfs()

    if not pdflist:
        showinfo("Done", f"No PDF files to combine")
        return

    merger = PyPDF2.PdfFileMerger()
    for pdf in pdflist:

        try:
            merger.append(pdf)
        except:
            # print(f"invalid PDF file {pdf}")
            showinfo("Error", f"Invalid PDF file {pdf}")

    directory = fd.askdirectory()
    if directory:
        name = input('Type name for the combined file:  ')
        new_file = directory + '/' + name + '.pdf'
        merger.write(new_file)
        showinfo("Done", f"Successfully Merged and saved as {name}.pdf")
    else:
        showinfo("Process Completed", f"No directory selected hence could not save combined File")




if __name__ == '__main__':
    pdf_combiner()
