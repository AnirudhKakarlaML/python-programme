#Smart Billing & Discount System
print(">>>>>>Smart Billing And Discount System<<<<<<<")
#Field Where Customer Inputs Are Required
product_name = str(input("Enter The Name Of The Product Purchased:-"))
product_price = float(input("Enter The Price Of The Purchased Product:-"))
quantity = int(input("No. Of Units Purchased:-"))
#Caluculation Of Total Price
total_price = product_price * quantity
#Membership Satus Check
areyou_amember = str(input("Are You A Member(Answer-Yes/No(-Capital Letter Mandatory At Start-)):-"))
#Price Finalisation
if(areyou_amember == "Yes" and  product_price>=1000):
    discount = 0.2
elif(areyou_amember == "Yes"  and product_price<1000):
    discount = 0.1
elif(areyou_amember == "No"  and product_price>=1000):
    discount = 0.05
else:
    discount=0.0
#Total Amount Declaration
discount_price=total_price*discount
final_price=total_price-discount_price
#Customer Review Slip
print(f"The Product You Purchased is :- {product_name}")
print(f"The Products Price from Manfacturer Is {product_price:.2f}")
print(f"No.of Units purchased:-{quantity}")
print(f"The MemberShip Status:-{areyou_amember}")
print(f"The Final Price After Discount Is {final_price:.2f}")