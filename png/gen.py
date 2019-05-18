from fpdf import FPDF
pdf = FPDF()
# https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images
for image in ["mix%d.png" % x for x in range(1, 16)]:
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)
pdf.output("mixed.pdf", "F")
