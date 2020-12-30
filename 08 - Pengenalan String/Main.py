data = "Ini String"
print(data)
print(type(data))

# 1. Cara membuat string

'''
      1. Dengan menggunakan single quote '..'
      2. Dengan menggunakan double quote ".."
'''
data = 'Ini single quote'
print(data)

data = "Ini double quote"
print(data)

print('"Halo?"')
print("'Halo?'")
print("ini adalah hari jum'at")


# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\Daffa")

# tab
print("Daffa\t\t\tSulthon, berjarak banyak")

# backspace
print("Daffa \bSulthon, jadi tanpa jarak")

# newline
print("baris pertama, \nbaris kedua.")
# \n -> LF (line feed) -> unix, macos, linux
print("baris pertama, \rbaris kedua.")
# \n -> CR (carriage return) -> commodore, acorn, lisp, yang dulu-dulu / bahasa lamas
print("baris pertama, \r\nbaris kedua.")
# \r\n -> CRLF (line feed carriage return) -> dipakai oleh windows


# 3. String literal atau raw

# hati-hati
print('C:\new folder')  # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Daffa
Alamat : Bogor
""")

# multiline literal string dan RAW
print(r"""
Nama : Daffa
Kelas : 12 SMA\new
Alamat : Bogor
Website : www.daffa.com/newID
""")
