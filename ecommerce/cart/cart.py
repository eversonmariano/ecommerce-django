
class Cart():

        def __init__(self, request):

            self.session = request.session

        # Returning user - obtain his/her existing session

            cart = self.session.get('session_key')

        # New user - generate a new session

            if 'session_key' not in self.session:
                cart = self.session['session_key'] = {}


            self.cart = cart


        def add(self, product, product_qty):

            product_id = str(product.id)

            if product_id in self.cart:
                self.cart[product_id]['qtd'] = product_qty

            else:
                self.cart[product_id] = {'price': str(product.price),'qtd': product_qty}


            self.session.modified = True

        def __len__(self):

            return sum(item['qtd'] for item in self.cart.values())