from django.shortcuts import render, redirect
from pymongo import MongoClient

# MongoDB connection settings
mongodb_uri = "mongodb://localhost:27017/"  # Replace with your MongoDB URI
database_name = "NJD"  # Replace with your database name
collection_name = "Programmers"  # Replace with your collection name

def index(request):
    try:
        client = MongoClient(mongodb_uri)
        db = client[database_name]
        collection = db[collection_name]
        data = list(collection.find())
        return render(request, 'index.html', {'data': data})
    except Exception as e:
        return render(request, 'error.html', {'error_message': f"An error occurred: {str(e)}"})
    finally:
        client.close()

def insert(request):
    if request.method == 'POST':
        try:
            client = MongoClient(mongodb_uri)
            db = client[database_name]
            collection = db[collection_name]

            name = request.POST['name']
            email = request.POST['email']
            age = int(request.POST['age'])

            data_to_insert = {
                "name": name,
                "email": email,
                "age": age,
            }

            inserted_id = collection.insert_one(data_to_insert).inserted_id
            return redirect('index')
        except Exception as e:
            return render(request, 'error.html', {'error_message': f"An error occurred: {str(e)}"})
        finally:
            client.close()

if __name__ == '__main__':
    pass
