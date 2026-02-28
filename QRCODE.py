import qrcode  #we did *pip install qrcode[pil]* on cmd terminal
upi_id = input("Enter your UPI ID: ")   #HERE YOU HAVE TO GIVE YOUR UPI ID TO THE USER
phonepay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
phonepay_qr=qrcode.make(phonepay_url)
paytm_qr=qrcode.make(paytm_url)
googlepay_qr=qrcode.make(googlepay_url)
phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
googlepay_qr.save('googlepay_qr.png')
phonepay_qr.show()
#THE IMAGE WILL POP UP THREE TIMES AS IT IS GENERATED FOR GPAY,PAYTM AND PHONEPAY ALL THREE
