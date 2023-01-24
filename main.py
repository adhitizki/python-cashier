# import libraries
from tabulate import tabulate
import re
from typing import List, Tuple

class Transaction:
    """
    Class untuk melakukan mencatat transaksi

    Parameters
    ----------
    data : dict
        Penyimpanan setiap detail data transaksi yang telah dilakukan.
        Pada dict memiliki struktur sebagai berikut:
        {
            'item' : {
                'item' : str,
                'jumlah_item' : int,
                'harga_item' : int,
                'total_harga' : int
            }
        }

    """
    def __init__(self):
        """
        Memulai transaksi dengan data kosong berupa format dict.

        Returns
        -------
        None

        """
        self.data = {}

    def add_item(self, items:List[Tuple[str, int, int]]):
        """
        Menambahkan item pada sebuah transaksi.

        Parameters
        ----------
        items : list
            List dari Tuple yang berisi detail item pada transaksi.
            Setiap Tuple harus terdiri dari 3 elemen yaitu:
                - string : item yang ingin ditambahkan.
                - int : banyak item yang ingin ditambahkan.
                - int : harga stauan pada item yang ingin ditambahkan.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            jika jenis format masukkan salah.      
        
        """
        try:
            # loop each item in list
            for (item, jumlah_item, harga_item) in items:
                # checking format input
                assert type(item)==str
                assert type(jumlah_item)==int
                assert type(harga_item)==int

                # checking item exist
                if item in self.data.keys():
                    print(f'{item} already exist in transaction')
                    continue

                else:
                    # add item detail to data
                    self.data[item] = {
                        'item' : item,
                        'jumlah_item' : jumlah_item,
                        'harga_item' : harga_item,
                        'total_harga' : jumlah_item * harga_item
                    }

            # print data
            data = [i for i in self.data.values()]
            print(tabulate(data, headers="keys", tablefmt="pipe"))
        
        except:
            print('Format masukkan salah')

    def update_item_name(self, item:str, update_nama_item:str):
        """
        Mengganti nama item.

        Parameters
        ----------
        item : str
            nama dari item yang ingin diganti.
        update_nama_item : str
            nama pengganti dari nama item sebelumnya.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            jika nama item yang ingin diganti tidak ada dalam transaksi.
        
        """
        try:
            # checking format input
            if (
                type(item)!=str or
                type(update_nama_item)!=str
            ):
                print('Format masukkan salah')

            else:
                # acess item
                temp = self.data[item].copy()

                # change name item
                temp['item'] = update_nama_item

                # delete unchanged item
                del self.data[item]

                # add updated
                self.data[update_nama_item] = temp

                # print data
                data = [i for i in self.data.values()]
                print(tabulate(data, headers="keys", tablefmt="pipe"))

        except:
            print('Item tidak terdapat dalam transaksi')

    def update_item_qty(self, item:str, update_jumlah_item:int):
        """
        Mengganti jumlah item.

        Parameters
        ----------
        item : str
            nama dari item yang ingin diganti jumlah itemnya.
        update_jumlah_item : str
            jumlah item baru.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            jika nama item yang ingin diganti tidak ada dalam transaksi.
        
        """
        try:
            # checking format input
            if (
                type(item)!=str or
                type(update_jumlah_item)!=int
            ):
                print('Format masukkan salah')

            else:
                # update quantity item
                self.data[item]['jumlah_item'] = update_jumlah_item
                self.data[item]['total_harga'] = update_jumlah_item * self.data[item]['harga_item']

                # print data
                data = [i for i in self.data.values()]
                print(tabulate(data, headers="keys", tablefmt="pipe"))

        except:
            print('Item tidak terdapat dalam transaksi')

    def update_item_price(self, item:str, update_harga_item:int):
        """
        Mengganti harga item.

        Parameters
        ----------
        item : str
            nama dari item yang ingin diganti harga itemnya.
        update_harga_item : str
            harga item baru.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            jika nama item yang ingin diganti tidak ada dalam transaksi.
        
        """
        try:
            # checking format input
            if (
                type(item)!=str or
                type(update_harga_item)!=int
            ):
                print('Format masukkan salah')

            else:
                # update quantity item
                self.data[item]['harga_item'] = update_harga_item
                self.data[item]['total_harga'] = self.data[item]['jumlah_item'] * update_harga_item

                # print data
                data = [i for i in self.data.values()]
                print(tabulate(data, headers="keys", tablefmt="pipe"))

        except:
            print('Item tidak terdapat dalam transaksi')

    def delete_item(self, item:str):
        """
        Menghapus item pada transaksi.

        Parameters
        ----------
        item : str
            nama dari item yang ingin dihapus pada transaksi.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            jika nama item yang ingin dihapus tidak ada dalam transaksi.
        
        """
        try:
            # checking format input
            if type(item)!=str:
                print('Format masukkan salah')

            else:
                # delete item
                del self.data[item]

                # print data
                data = [i for i in self.data.values()]
                print(tabulate(data, headers="keys", tablefmt="pipe"))

        except:
            print('Item tidak terdapat dalam transaksi')

    def reset_transaction(self):
        """
        Data transaksi dikembalikan seperti awal atau dikosongkan.

        Returns
        -------
        None
        
        """
        # reset all data
        self.data = {}
        print('Transaksi kembali ke setelan awal')

    def check_order(self):
        """
        Pengecekan masukkan untuk setiap item transaksi.

        Memberikan penjelasan untuk masukkan yang sudah benar atau belum.
        Serta memperlihatkan detail transaksi dengan format tabular data.

        Returns
        -------
        None
        
        """
        # check if no order
        if len(self.data)==0:
            print('item tidak terdapat dalam transaksi')

        # check input each items
        else:
            false_input = set()
            for items in self.data.values():

                # check items input
                temp_item = items['item']
                temp_item = re.sub(r'[\s\']+', '', temp_item)

                if not temp_item.isalnum():
                    false_input.add('Variabel items tidak bersih')

                # check quantity              
                if items['jumlah_item']<=0:
                    false_input.add('Variabel jumlah_item kurang dari sama dengan 0')

                # check price
                if items['harga_item']<=0:
                    false_input.add('Variabel harga_item kurang dari sama dengan 0')

            # print checking inputs
            if len(false_input)>0:
                print(f'Kesalahan masukkan terdeteksi terdapat pada {tuple(false_input)}\n')

            else:
                print('Masukkan benar\n')

        # print data
        data = [i for i in self.data.values()]
        print(tabulate(data, headers="keys", tablefmt="pipe"))

    def total_price(self):
        """
        Menghitung jumlah total harga pada transaksi, serta perhitungan sudah termasuk dengan diskon yang berlaku.

        Returns
        -------
        None

        """
        # calculate total price
        list_harga = [i['total_harga'] for i in self.data.values()]
        total_harga_semua = sum(list_harga)

        # discount calculation
        discounts = [
            (0.9, 500000),
            (0.92, 300000),
            (0.95, 200000)
        ]

        for discount, threshold in discounts:
            if total_harga_semua > threshold:
                total_harga_semua = total_harga_semua * discount
                break

        print(f'Jumlah keseluruhan harga pada transaksi sebesar Rp.{int(total_harga_semua)}\n')

        # print data
        data = [i for i in self.data.values()]
        print(tabulate(data, headers="keys", tablefmt="pipe"))


