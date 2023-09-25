student = {
"nama" : "faqih",
"umur" : 26,
"tinggi" : 177.6
}
print(student)
student.pop("umur")
print(student)

# Output
# {'nama': 'faqih', 'umur': 26, 'tinggi': 177.6}
# {'nama': 'faqih', 'tinggi': 177.6}