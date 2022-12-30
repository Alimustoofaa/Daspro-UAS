import os
import db
import pymongo
import pandas as pd

category_list = ['pengeluaran', 'pemasukan']

def get_all():
    collection = db.connect_db()
    object_id = collection.find({"data_cat": 'uas'}).sort([('date', pymongo.DESCENDING)])
    output_data = list()
    for data in object_id:
        data_a = list()
        for k, v in data.items():
            if k in ['id', 'total', 'category', 'date']:
                data_a.append(v if not k == 'category' else category_list[v])
        output_data.append(data_a)

    data_pd = pd.DataFrame(output_data, columns=['id', 'total', 'category', 'date'], index=list(' '*len(output_data)))
    print('='*50)
    print(data_pd)
    print('='*50)

def get_one(id):
    collection = db.connect_db()
    query = {'$and': [
            {"id": id},
            {'data_cat': 'uas'}
        ]}
    try:  
        object_id = collection.find(query).limit(1).next()
        return object_id
    except StopIteration:
        os.system('clear')
        print(f'Data Dengan ID {id} Tidak Ditemukan !!')
        return None

def insert(total, category, date):
    collection = db.connect_db()
    # find last id
    last_id = collection.find({}, {"id": 1}, sort=[('id', -1)]).limit(1).next()  
    last_id['id'] += 1
    # data inset
    data = {
        'data_cat': 'uas',
        'id' : last_id['id'],
        'total': total,
        'category': category_list.index(category),
        'date': date

    }
    # inset data
    insert = collection.insert_one(data)
    if not insert.acknowledged:
        print('Gagal Menambahkan data')
        return False
    else:
        print('='*50)
        print('Data Berhasil Ditambahkan')
        print('='*50)
        output_data = list()
        for k, v in data.items():
            if k in ['id', 'total', 'category', 'date']:
                    output_data.append(v if not k == 'category' else category_list[v])
        data_pd = pd.DataFrame([output_data], columns=['id', 'total', 'category', 'date'], index=[''])
        print(data_pd)
        print('='*50)

def update(id, total, category, date):
    collection = db.connect_db()
    # data inset
    data = {
        'total': total,
        'category': category_list.index(category),
        'date': date

    }
    # inset data
    update = collection.find_one_and_update(
        {'id' : id},
        {'$set': data}
    )
    if not update:
        print(f'Data Id {id} Gagal Diedit')
        return False
    else:
        print('='*50)
        print(f'Data Id {id} Berhasil diedit')
        print('='*50)
        output_data = list()
        for k, v in data.items():
            if k =='total': output_data.insert(1, v)
            if k =='category': output_data.insert(2, category_list[v])
            if k =='date': output_data.insert(3, v)
        data_pd = pd.DataFrame([output_data], columns=['total', 'category', 'date'], index=[''])
        print(data_pd)
        print('='*50)
        return True

def delete(id):
    collection = db.connect_db()
    query = {'$and': [
                {"id": id},
                {'data_cat': 'uas'}
            ]}  
    object_id = collection.delete_one(query)
    if object_id.deleted_count > 0:
        print(f'Data dengan ID {id} Berhasil Dihapus')
        return True
    else:
        print(f'Data dengan ID {id} Tidak Ditemukan Dihapus')
        return False

def total_transaksi():
    collection = db.connect_db()
    object_id = collection.find({"data_cat": 'uas'}).sort([('date', pymongo.DESCENDING)])
    
    total_income, total_outcome = 0, 0
    for data in object_id:
        if data['category'] == category_list.index('pengeluaran'):
            total_outcome += data['total']
        elif data['category'] == category_list.index('pemasukan'):
            total_income += data['total']
        
    # Calculate Saldo
    saldo = total_income - total_outcome

    data_pd = pd.DataFrame([[total_income, total_outcome, saldo]], columns=['pemasukan', 'pengeluaran', 'saldo'], index=[''])
    print('='*50)
    print(data_pd)
    print('='*50)