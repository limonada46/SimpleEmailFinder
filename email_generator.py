filename = str(input("Enter the filename that will be created: ")) + ".txt"
first_name = str(input("Enter the first name of the person: "))
last_name = str(input("Enter the last name of the person: "))
domain = str(input("Enter the @domain of the person, example: @mantech.com "))

possible_emails = []

#Coding the possible emails and appending them to the list possible emails

email = first_name + last_name + domain
possible_emails.append(email)

email = first_name[0] + last_name + domain
possible_emails.append(email)

email = first_name + "." + last_name + domain
possible_emails.append(email)

email = first_name[0] + "." + last_name + domain
possible_emails.append(email)

email = first_name + "_" + last_name + domain
possible_emails.append(email)

email = first_name[0] + "_" + last_name + domain
possible_emails.append(email)

email = last_name + first_name + domain
possible_emails.append(email)

email = last_name + first_name[0] + domain
possible_emails.append(email)

email = last_name + "." + first_name + domain
possible_emails.append(email)

email = last_name + "." + first_name[0] + domain
possible_emails.append(email)

email = last_name + "_" + first_name + domain
possible_emails.append(email)

email = last_name + "_" + first_name[0] + domain
possible_emails.append(email)

results = " \n".join(possible_emails)

with open(filename, "w") as file:
    file.write(results)
    print("The program has finished, thanks for using this program!")