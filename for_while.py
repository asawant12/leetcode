guest1="deshpande"
guest2="ladkat"
guest_list = ["dehpande", "ladkat","tengshe"]

for guest_name in guest_list:
  print(guest_name)

index = 0

while index < len(guest_list):
  print(guest_list[index])
  index = index + 1

guest_list.append("Tathode")
guest_list.append("Khade")

print(guest_list)
