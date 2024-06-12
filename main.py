from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_receipt(receipt_data, filename):
    """
    Create a PDF receipt using the provided receipt data.
    
    :param receipt_data: A dictionary containing receipt details.
    :param filename: The name of the file to save the PDF as.
    """
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "Payment Receipt")

    # Receipt details
    c.setFont("Helvetica", 12)
    text_lines = [
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Receipt Number: {receipt_data['receipt_number']}",
        f"Customer Name: {receipt_data['customer_name']}",
        f"Amount Paid: ${receipt_data['amount']:.2f}",
        f"Payment Method: {receipt_data['payment_method']}",
        f"Description: {receipt_data['description']}"
    ]
    
    y = height - 100
    for line in text_lines:
        c.drawString(50, y, line)
        y -= 20

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 50, "Thank you for your business!")
    
    c.showPage()
    c.save()

if __name__ == "__main__":
    receipt_data = {
        "receipt_number": "123456",
        "customer_name": "John Doe",
        "amount": 250.00,
        "payment_method": "Credit Card",
        "description": "Purchase of electronics"
    }
    
    filename = "receipt.pdf"
    create_receipt(receipt_data, filename)
    print(f"Receipt saved as {filename}")
