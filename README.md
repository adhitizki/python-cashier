# Latar Belakang
Pada setiap pembelian atau transaksi perlu pelacakan item atau barang apa saja yang sudah dibeli. Terutama pada kasus supermarket atau pusat perbelanjaan yang besar dimana sudah banyak barang dan pembeli yang memerlukan pelacakan transaksi untuk memudahkan kasir atau penjual dalam melacak transaksi yang ada. Dengan program kasir ini diharapkan penjual dapat melakukan pelacakan transaksi pada pembeli serta perhitungan harga total belanja yang sudah menerapkan syarat dan ketentuan untuk yang mendapatkan potongan harga.

# Tools
Bahasa Pemograman:
* Python 3.9

Libraries:
* Tabulate 0.9.0
* Regex

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

# Penjelasan Code
- Pada script *'main.py'* terdapat *class* bernama `Transaction` yang berfungsi untuk mencatat item pembelian oleh seorang pembeli. Pada *class* `Transaction` memiliki beberapa method diantaranya:
    * `__init__()`
    * `add_item()`
    * `update_item_name()`
    * `update_item_qty()`
    * `update_item_price()`
    * `delete_item()`
    * `reset_transaction()`
    * `check_order()`
    * `total_price()`

    <img src="img\class_transaction.svg" width="500"/>

- Pada script juga *import libraries* diantaranya:
    * tabulate : berfungsi *print* data rapi atau secara gaya *tabular data*.
    * re : Regex berfungsi untuk melakukan pengecekan nama item terdapat symbol atau tidaknya (bersih tidaknya masukkan nama item).
    * typing : berfungsi untuk memberikan arahan pada masukkan yang seharusnya.

    <img src="img\libraries.svg" width="500"/>

- Method `__init__()` berfungsi sebagai inisiasi pada *class* `Transaction` dengan memberikan *attribute* berupa data kosong dengan format *dict*. pada penyimpanan data memiliki struktur sebagai berikut:
```
{
    'item' : {
        'item' : str,
        'jumlah_item' : int,
        'harga_item' : int,
        'total_harga' : int
    }
}
```
- Dengan nama item digunakan sebagai *keys* pada penyimpanan tersebut sehingga saat ingin memanggil detail item maka pemanggilan data menggunakan nama item. Hal ini seperti SKU atau barcode pada database supermarket.

    <img src="img\method_init.svg" width="500"/>

- Method `add_item()` digunakan untuk menambahkan detail item pada transaksi. Dengan masukkan method tersebut berupa *list* yang berisi *tuple*. Dengan *tuple* harus terdiri dari 3 elemen yaitu nama item berupa *string*, jumlah item berupa *integer* dan harga item berupa *integer*. Pada method tersebut juga mengidentifikasi kesesuaian tipe format masukkan, serta mengidentifikasi nama item yang sama. Jika format masukkan salah dan item sudah ada sebelumnya pada transaksi, method tersebut akan memberitahu kesalahannya.

    <img src="img\method_add_item.svg" width="500"/>

- Method `update_item_name()` digunakan untuk mengganti atau memperbarui nama item. Dengan masukkan method tersebut berupa nama item yang ingin diubah dan nama item yang baru. Masukkan harus berupa format *string*. Penggantian nama dilakukan dengan cara mengakses detail item lama, kemudian di *copy* dan dimasukkan kembali kedalam data transaksi dengan nama item baru dan kata kunci atau *keys* pada data transaksi sesuai dengan nama item baru. Dengan data pada item lama dihapus pada data transaksi. Pada method tersebut juga mengidentifikasi format masukkan dan mengecek ketersediaan item pada data transaksi. Jika tidak maka akan memberitahukan kesalahannya.

    <img src="img\method_update_item_name.svg" width="500"/>

- Method `update_item_qty()` digunakan untuk mengganti atau memperbarui jumlah item. Dengan masukkan method tersebut berupa nama item yang ingin diubah jumlah itemnya. Masukkan harus berupa format *string* pada nama item dan *integer* pada jumlah item barunya. Penggantian jumlah item dilakukan dengan cara mengakses data item tersebut dengan *key* nama item, lalu langsung mengubah jumlah itemnya serta total harga pada item tersebut. Pada method tersebut juga mengidentifikasi format masukkan dan mengecek ketersediaan item pada data transaksi. Jika tidak sesuai maka akan memberitahukan kesalahannya.

    <img src="img\method_update_item_qty.svg" width="500"/>

- Method `update_item_price()` digunakan untuk mengganti atau memperbarui harga item. Dengan masukkan method tersebut berupa nama item yang ingin diubah harga itemnya. Masukkan harus berupa format *string* pada nama item dan *integer* pada harga item barunya. Penggantian harga item dilakukan dengan cara mengakses data item tersebut dengan *key* nama item, lalu langsung mengubah harga itemnya serta total harga pada item tersebut. Pada method tersebut juga mengidentifikasi format masukkan dan mengecek ketersediaan item pada data transaksi. Jika tidak sesuai maka akan memberitahukan kesalahannya.

    <img src="img\method_update_item_price.svg" width="500"/>

- Method `delete_item()` digunakan menghapus sebuah item pada data transaksi. Masukkan harus berupa format *string* yang mana merupakan nama item yang ingin dihapus. Proses penghapusan menggunakan perintah *del* pada data transaksi dengan *key* berupa nama item masukkan. JIka masukkan tidak sesuai format atau nama item tidak ada pada data transaksi, maka program akan memberitahukan kesalahannya.

    <img src="img\method_delete_item.svg" width="500"/>

- Method `reset_transaction()` digunakan untuk menghapus semua item dalam data transaksi atau ingin mengembalikan kondisi awal data transaksi (kosong). Saat penggunaan method tersebut maka data akan di definisikan dengan *dict*

    <img src="img\reset_transaction.svg" width="500"/>

- Method `check_order()` digunakan untuk mengecek masukkan sebelumnya pada data transaksi yang sudah tersimpan. Method tersebut memiliki beberapa kondisi pengecekan diantaranya:
    * Jika tidak ada data maka akan menghasilkan keluaran berupa 'Item tidak terdapat dalam transaksi'.
    * Pengecekan tiap nama item dengan nama variabel tidak memiliki karakter selain alfanumerik, spasi (*whitespace*), dan tanda petik ( ' )
    * Pengecekan tiap jumlah item dengan kondisi harus diatas 0.
    * Pengecekan tiap harga item dengan kondisi harus diatas 0.
    * Notifikasi berupa *print* jika masukkan benar atau salah
    * Memperlihatkan data transaksi tersimpan.

    <img src="img\check_order.svg" width="500"/>

- Method `total_price()` digunakan untuk menghitung harga keselurhan item pada data transaksi. pada method juga menerapkan potongan harga dengan kondisi tertentu. Proses tersebut dilakukan dengan melakukan looping pada batas harga yang mendapat potongan dan persentase harga yang dibayarkan. Jika memenuhi dengan batas harga maka akan menghitung harga setelah mendapat potongan dan looping akan berhenti.

    <img src="img\total_price.svg" width="500"/>

# Hasil Test Case
1. Memanggil Class

    <img src="img\test_1_import.jpg" width="500"/>

2. Menambahkan Item

    <img src="img\test_2_add_item.jpg" width="500"/>

3. Update Nama Item

    <img src="img\test_3_update_item.jpg" width="500"/>

4. Update Jumlah Item

    <img src="img\test_4_update_qty.jpg" width="500"/>

5. Update Harga Item

    <img src="img\test_5_update_price.jpg" width="500"/>

6. Hapus Item

    <img src="img\test_6_delete_item.jpg" width="500"/>

7. Reset Transaksi

    <img src="img\test_7_reset.jpg" width="500"/>

8. Check Order

    <img src="img\test_8_check.jpg" width="500"/>

9. Total Keseluruhan Harga

    <img src="img\test_9_total.jpg" width="500"/>

# Rangkuman dan Saran

- Program mampu menjalankan tugas sistem kasir sederhana atau CRUD sederhana.
- Dapat mengembangkan program lebih kompleks dengan menggunakan database sebagai penyimpanan serta `unique_id` menggunakan SKU atau *barcode* alih-alih menggunakan nama item.
- Perbaikan lanjutan jika diketemukan `bug` dikemudian hari.