text = "We are learning Python for DevOps"

new_text = text.split()

print("Splitting text: ", new_text)

print( text.split( )[3])

arn = "arn:partition:service:region:account-id:resource-type/resource-id"

new_arn = arn.split("/")

print("Display arn: ", new_arn)

print("Displaying Object 1", arn.split("/")[0])

print("Displaying Object 2", arn.split("/")[1])