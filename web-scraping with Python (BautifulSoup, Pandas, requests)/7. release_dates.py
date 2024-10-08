# Get all elements in the product row
all_elements = soup.select('.a-row .a-size-base.a-color-secondary.a-text-normal')

# Print all to inspect
for element in all_elements:
    print(element.text.strip())

# outcome
# Dec 10, 2023
# Oct 1, 2022
# Oct 22, 2021
# Sep 15, 2023
# Jan 26, 2024
# Feb 1, 2024
# Jul 19, 2024
# Feb 1, 2024
# Oct 11, 2024
# Feb 21, 2024
# Oct 20, 2023
# Aug 16, 2024
# Feb 1, 2024
#This already is useful data in case you are looking for release dates
