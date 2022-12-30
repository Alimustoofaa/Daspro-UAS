import os
import datetime
import controller

category_list = ['pengeluaran', 'pemasukan']

def insert_action():
    while True:
        while True:
            category_input = input(f'Masukkan Kategori [Pemasukan/Pengeluaran] : ')
            if category_input not in category_list:
                print(f'Kategori {category_input} Tidak Valid !!')
            else: break
        # Input jumlah
        total_input = int(input(f'Masukkan Total : '))
        # Input and validation tanggal
        while True:
            date_input  = input(f'Masukkan Tanggal [dd/mm/yyyy] : ')
            try:
                if type(date_input) == str:
                    date_input = datetime.datetime.strptime(date_input, '%d/%m/%Y')
            except ValueError:
                print('Input Tanggal Tidak Valid eg. 30/12/2022')
            else:
                break
        controller.insert(category=category_input, total=int(total_input), date=date_input)
        next_input = input('Apakah Anda Ingin Memasukkan Data Lagi? [y/n] : ')
        if next_input.lower() == 'n':os.system('clear');break
        os.system('clear')

def update_action():
    while True:
        controller.get_all()
        id_input = int(input('Masukkan ID Untuk Mengedit Data : '))
        get_data = controller.get_one(id_input)
        if get_data:
            print('Kosongi Input Jika Tidak Ingin Mengedit Data !!')
            # Input and validation category
            while True:
                category_input = input(f'Edit Kategori {category_list[get_data["category"]]} ke ') or category_list[get_data["category"]]
                if category_input not in category_list:
                    print(f'Kategori {category_input} Tidak Valid !!')
                else: break
            # Input jumlah
            total_input = int(input(f'Edit Jumlah {get_data["total"]} ke ') or get_data["total"])
            # Input and validation tanggal
            while True:
                date_input  = input(f'Edit Tanggal {get_data["date"]} ke ') or get_data["date"]
                try:
                    if type(date_input) == str:
                        date_input = datetime.datetime.strptime(date_input, '%d/%m/%Y')
                except ValueError:
                    print('Input Tanggal Tidak Valid eg. 30/12/2022')
                else:
                    break
            controller.update(id=int(id_input), category=category_input, total=int(total_input), date=date_input)
            next_input = input('Apakah Anda Ingin Mengedit Data Lagi? [y/n] : ')
            if next_input.lower() == 'n': os.system('clear'); break
            os.system('clear')

def delete_action():
    while True:
        controller.get_all()
        id_input = int(input('Masukkan ID Untuk Menghapus Data : '))
        get_data = controller.get_one(id_input)
        if get_data:
            controller.delete(id_input)
        next_input = input('Apakah Anda Ingin Menghapus Data Lagi? [y/n] : ')
        if next_input.lower() == 'n':os.system('clear'); break
        os.system('clear')

def show_all_action():
    while True:
        controller.get_all()
        next_input = input('Apakah Anda Ingin Menamilkan Data Lagi? [y/n] : ')
        if next_input.lower() == 'n':os.system('clear'); break
        os.system('clear')

def total_action():
    while True:
        controller.total_transaksi()
        next_input = input('Apakah Anda Ingin Menamilkan Data Lagi? [y/n] : ')
        if next_input.lower() == 'n':os.system('clear'); break
        os.system('clear')


menu_dict = {
    1: 'Menambahkan Pemasukan/Pengeluaran',
    2: 'Edit Data Pemasukan/Pengeluaran',
    3: 'Delete Data Pemasukan/Pengeluaran',
    4: 'Menampilkan Data Transaksi',
    5: 'Menampilkan Total  Transaksi',
    0: 'EXIT'
}
def print_menu():
    print('ID     MENU')
    for k,v in menu_dict.items():
        print(f'[{k}] : {v}')

while True:
    print_menu()
    input_menu = int(input('Masukkan ID Menu : '))
    if input_menu not in menu_dict.keys():
        print('Menu ID Tidak Valid !!')
        os.system('clear')
    elif input_menu == 1:
        os.system('clear')
        insert_action()
    elif input_menu == 2:
        os.system('clear')
        update_action()
    elif input_menu == 3:
        os.system('clear')
        delete_action()
    elif input_menu == 4:
        os.system('clear')
        show_all_action()
    elif input_menu == 5:
        os.system('clear')
        total_action()
    elif input_menu == 0:
        break
