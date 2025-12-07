def read_product(product_id):
    return {"id": product_id, "name": "Sample Product"}

def update_product(product_id, data):
    return {"id": product_id, "name": data.get("name", "Sample Product")}

def delete_product(product_id):
    return {"message": f"Product {product_id} deleted"}

def list_all_products():
    return [{"id": 1, "name": "Sample Product"}]

def list_by_name(name):
    return [{"id": 1, "name": name}]

def list_by_category(category):
    return [{"id": 1, "category": category}]  

def list_by_availability(available=True):
    return [{"id": 1, "available": available}]
