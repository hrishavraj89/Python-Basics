# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

class Employee:
    company = "Google"

    def work(hri):
        print(f"The name of the commpany is {hri.company}.")

hri = Employee()
hri.work()

# Yes, we can use anything instead of 'self' parameter, but using self is considered a good practice.
# So, we use self!!