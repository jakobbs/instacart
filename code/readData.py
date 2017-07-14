#read data

types = {'reordered':np.float16,
'add_to_cart_order':np.float16,
'order_id':np.uint32,
'product_id':np.uint16,
'days_since_prior_order': np.float16,
'user_id':np.uint32,
'order_dow':np.float16,
'order_hour_of_day':np.float16,
'order_number': np.float16,
'aisle_id':np.float16,

}




aisles = pd.read_csv('../data/aisles.csv',dtype=types)
print("Shape aisles:", aisles.shape)

departments = pd.read_csv('../data/departments.csv',dtype=types)
print("Shape departments:", departments.shape)

order_products__prior = pd.read_csv('../data/order_products__prior.csv',dtype=types)

print("Shape order_products__prior:", order_products__prior.shape)

order_products__train = pd.read_csv('../data/order_products__train.csv',dtype=types)
print("Shape order_products__train:", order_products__train.shape)

orders = pd.read_csv('../data/orders.csv',dtype=types)
print("Shape orders:", orders.shape)

products = pd.read_csv('../data/products.csv',dtype=types)
print("Shape products:", products.shape)

