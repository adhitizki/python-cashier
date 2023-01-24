# Latar Belakang
Pada setiap pembelian atau transaksi perlu pelacakan item atau barang apa saja yang sudah dibeli. Terutama pada kasus supermarket atau pusat perbelanjaan yang besar dimana sudah banyak barang dan pembeli yang memerlukan pelacakan transaksi untuk memudahkan kasir atau penjual dalam melacak transaksi yang ada. Dengan program kasir ini diharapkan penjual dapat melakukan pelacakan transaksi pada pembeli serta perhitungan harga total belanja yang sudah menerapkan syarat dan ketentuan untuk yang mendapatkan potongan harga.

# Requirements / Objectives
1. Membuat program kasir sederhana untuk melakukan pelacakan transaksi.
2. Mampu menerapkan CRUD sederhana pada program kasir sederhana.
3. Membuat proses total_harga yang menghitung keseluruhan transaksi dan menerapkan kondisi tertentu untuk potongan harga.
4. Mampu mengimplementasikan OOP pada program.
5. Mampu membuat dokumentasi docstring pada program.
6. Mampu mengimplementasikan *defense programming.*
7. Mampu mengimpelemntasikan *clean code* dan *modular code.*

# Alur Program
1. Unduh file main.py lalu tempatkan file pada direktori lokal.

2. Buka jupyter notebook atau IDE python dengan lokasi yang sama pada file main.py

3. Import transaction class pada file main.py
```
from main import Transaction
```

4. Membuat instance dari Transaction class.
```
transaksi = Transaction()
```

5. Untuk menambahkan item kedalam data transaksi, gunakan `add_item()` dengan cara mendefinisikan tuple yang terdiri (nama item, jumlah item, harga item) kedalam list.
```
items = [
    ('Apel', 1, 10000),
    ('Daging Sapi', 2, 150000),
    ('Spatula', 1, 30000)
]
transaksi.add_item(items)
```

6. Jika ingin mengganti atau memperbarui nama item, gunakan `update_item_name()`. Dengan memasukkan nama item dan nama item terbaru.
```
transaksi.update_item_name('Apel', 'Apel Malang')
```

7. Jika ingin mengganti atau memperbarui jumlah item, gunakan `update_item_qty()`. Dengan memasukkan nama item dan jumlah item terbaru.
```
transaksi.update_item_qty('Daging Sapi', 1)
```

8. Jika ingin mengganti atau memperbarui harga item, gunakan `update_item_price()`. Dengan memasukkan nama item dan harga item terbaru.
```
transaksi.update_item_price('Spatula', 25000)
```

9. Jika ingin menghapus item pada transaksi, gunakan `delete_item()` dengan memasukkan nama item.
```
transaksi.delete_item('Apel Malang')
```

10. Jika ingin mengulangi kembali transaksi atau mengembalikan data transaksi ke setelan awal gunakan `reset_transaction()`
```
transaksi.reset_transaction()
```

11. Ketika sudah melakukan transaksi maka perlu pengecekan pada daftar belanjaan untuk mengetahui terdapat masukkan yang salah atau tidak, terutama pada tipe data masukkan. Maka gunakan `check_order()`.
```
transaksi.check_order()
```

12. Ketika sudah mengecek dan ingin mengetahui total harga item pada transaksi gunakan `total_price()`. Dengan method tersebut sudah menerapkan kondisi untuk mendapat potongan harga.
```
transaksi.total_price()
```