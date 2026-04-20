# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"
if product_type == "Perishable":
  if days_until_expiration >= 3      and stock_level > 50: print("30% discount is applied")
  elif days_until_expiration >= 4    and  days_until_expiration <= 6     and stock_level > 50:   print("20% discount is applied")
  
  elif days_until_expiration > 6     and stock_level >50: print("10% discount is applied")
  




else:
	 print("no discount availale for non prishable pruduct")