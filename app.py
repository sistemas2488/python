from flask import Flask, jsonify, request

from products import products
app=Flask(__name__ )


@app.route('/ping',methods=['GET'])
def ping():
    return jsonify({"message":"Funciona"})

@app.route('/products',methods=['GET'])
def getProducts():
    return jsonify({"products": products,",message":"Lista de productos"})

@app.route('/products/<string:product_name>',methods=['GET'])
def getProduct(product_name):
    product_found=[product for product in products if product['name']==product_name ]
    if(len(product_found)>0):
        return jsonify({"products":product_found[0]})
    else:
         return jsonify({"message": "product not found"})
    
@app.route('/sendproducts',methods=['POST'])
def addProduct():
    new_product = {
        "name":request.json['name'],
        "price":request.json['price'],
        "quantity":request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "product added sussefuly","products":products})

@app.route('/products/<string:product_name>',methods=['PUT'])
def editProduct(product_name):
    product_found=[product for product in products if product['name']==product_name ]
    if(len(product_found)>0):
        product_found[0]['name']=request.json['name']
        product_found[0]['price']=request.json['price']
        product_found[0]['quantity']=request.json['quantity']
        return jsonify({"message": "product update sussefuly","products":products})
    return jsonify({"message": "product not found"})
        
@app.route('/products/<string:product_name>',methods=['DELETE'])
def deleteProduc(product_name):
    product_found=[product for product in products if product['name']==product_name ]
    if(len(product_found)>0):
        products.remove(product_found[0])
        return jsonify({"message": "product delete sussefuly","products":products})
    return jsonify({"message": "product not found"})





if __name__=='__main__':
    app.run(debug=True, port=4000)