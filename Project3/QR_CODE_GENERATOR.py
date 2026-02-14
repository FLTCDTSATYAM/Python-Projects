import qrcode

#Create UPI ID by providing it as input by user
upi_id = input("Enter your UPI ID: ")

#Connecting upi id 
phone_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name"

#Create QR code for each payment app
phone_pay_qr = qrcode.make(phone_pay_url)
paytm_qr = qrcode.make(paytm_url)

#Display the qr code(need to install PIL/pillow library)
phone_pay_qr.show()
paytm_qr.show()
