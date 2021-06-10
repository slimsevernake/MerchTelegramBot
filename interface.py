# Import Bot Module
import database as db
import query as q
import keyboard_bot as key
import required as req
# Import Python Module
import re
import threading
from time import sleep

bot = req.bot


class InterfaceInteraction(classmethod):
    def alert(self, message=None):
        bot.answer_callback_query(self.id, show_alert=False, text=message)

    def display_category(self):
        try:
            connection = db.create_connection(
                "merch_telegram_bot_db", "postgres", "Qsf98%x$", "127.0.0.1",
                "5432"
            )
            category = db.execution_of_requests(connection,
                                                q.interface_query['category'])
            if not category:
                bot.send_message(self.chat.id,
                                 "Категории товаров отсутствуют 😔")
            else:
                category = key.show_category(category)
                bot.send_message(self.chat.id,
                                 "Выберите раздел, чтобы вывести "
                                 "список товаров:",
                                 reply_markup=category)
            connection.close()
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return

    def display_cart(self):
        try:
            connection = db.create_connection(
                "merch_telegram_bot_db", "postgres", "Qsf98%x$",
                "127.0.0.1",
                "5432"
            )
            query = q.interface_query[
                        'display_product_cart'] + str(self.from_user.id)
            response = db.execution_of_requests(connection, query)
            cart = list(set(response))
            if cart == [(None, None, None, None, None)]:
                bot.send_message(self.chat.id, "В корзине пусто 😔")
            elif len(cart) == 1:
                index = 0
                quantity = len([i for i, x in enumerate(response)
                                if x == cart[index]])
                cart_keyboard = key.cart_keyboard_min(index, quantity)
                bot.send_message(self.chat.id, "Корзина:\n")
                bot.send_message(self.chat.id, f"{cart[index][1]}\n"
                                               f"{cart[index][2]}\n"
                                               f"<a href='{cart[index][4]}'>"
                                               f"&#8203;</a>",
                                 parse_mode="HTML",
                                 reply_markup=cart_keyboard)
            else:
                cart = sorted(cart)
                index = 0
                quantity = len([i for i, x in enumerate(response)
                                if x == cart[index]])
                prev_item = cart.index(cart[index - 1])
                next_item = cart.index(cart[index + 1])
                quantity_product = (len(cart) - 1)
                cart_keyboard = key.cart_keyboard(prev_item, next_item, index,
                                                  quantity, quantity_product)
                bot.send_message(self.chat.id, "Корзина:\n")
                bot.send_message(self.chat.id, f"{cart[index][1]}\n"
                                               f"{cart[index][2]}\n"
                                               f"<a href='{cart[index][4]}'>"
                                               f"&#8203 "
                                               f";</a>",
                                 parse_mode="HTML",
                                 reply_markup=cart_keyboard)
                connection.close()
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return

    def cart(self, delete=None):
        try:
            connection = db.create_connection(
                "merch_telegram_bot_db", "postgres", "Qsf98%x$",
                "127.0.0.1",
                "5432"
            )
            query = q.interface_query[
                        'display_product_cart'] + str(self.from_user.id)
            response = db.execution_of_requests(connection, query)
            cart = list(set(response))
            if cart == [(None, None, None, None, None)]:
                bot.edit_message_text(chat_id=self.message.chat.id,
                                      message_id=self.message.message_id,
                                      text="В корзине пусто 😔")
            elif len(cart) == 1:
                index = 0
                quantity = len([i for i, x in enumerate(response)
                                if x == cart[index]])
                cart_keyboard = key.cart_keyboard_min(index, quantity)
                bot.edit_message_text(chat_id=self.message.chat.id,
                                      message_id=self.message.message_id,
                                      text=f"{cart[index][1]}\n"
                                           f"{cart[index][2]}\n"
                                           f"<a href='{cart[index][4]}'>&#8203"
                                           f";</a>",
                                      parse_mode="HTML",
                                      reply_markup=cart_keyboard)
            else:
                index_str = extract_id(self.data)
                index = int(index_str[1])
                cart = sorted(cart)
                prev_item = cart.index(cart[index - 1])
                if index == cart.index(cart[-1]):
                    next_item = cart.index(cart[index - (len(cart) - 1)])
                    quantity = len([i for i, x in enumerate(response)
                                    if x == cart[index]])
                    quantity_product = (len(cart) - 1)
                    cart_keyboard = key.cart_keyboard(prev_item, next_item,
                                                      index,
                                                      quantity,
                                                      quantity_product)
                elif delete is True:
                    index = 0
                    next_item = cart.index(cart[index - (len(cart) - 1)])
                    quantity = len([i for i, x in enumerate(response)
                                    if x == cart[index]])
                    quantity_product = (len(cart) - 1)
                    cart_keyboard = key.cart_keyboard(prev_item, next_item,
                                                      index,
                                                      quantity,
                                                      quantity_product)
                else:
                    next_item = cart.index(cart[index + 1])
                    quantity = len([i for i, x in enumerate(response)
                                    if x == cart[index]])
                    quantity_product = (len(cart) - 1)
                    cart_keyboard = key.cart_keyboard(prev_item, next_item,
                                                      index,
                                                      quantity,
                                                      quantity_product)
                bot.edit_message_text(chat_id=self.message.chat.id,
                                      message_id=self.message.message_id,
                                      text=f"{cart[index][1]}\n"
                                           f"{cart[index][2]}\n"
                                           f"<a href='{cart[index][4]}'>&#8203"
                                           f";</a>",
                                      parse_mode="HTML",
                                      reply_markup=cart_keyboard)
            connection.close()
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return

    def delete_product(self):
        try:
            connection = db.create_connection(
                "merch_telegram_bot_db", "postgres", "Qsf98%x$",
                "127.0.0.1",
                "5432"
            )
            query = q.interface_query[
                        'display_product_cart'] + str(self.from_user.id)
            response = db.execution_of_requests(connection, query)
            cart = sorted(list(set(response)))
            index_str = extract_id(self.data)
            index = int(index_str[1])
            product_id = cart[index][0]
            query = f"""DELETE FROM cart_product WHERE 
            cart_product.cart_id = (SELECT cart_id FROM cart WHERE 
            cart.customer_id=(SELECT customer_id FROM customer WHERE 
            customer.chat_id = {self.message.chat.id})) AND cart_product
            .product_id = {product_id} """
            db.execution_of_requests(connection, query)
            connection.close()
            InterfaceInteraction.cart(self, delete=True)
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return

    def add_product(self):
        try:
            connection = db.create_connection(
                "merch_telegram_bot_db", "postgres", "Qsf98%x$",
                "127.0.0.1",
                "5432"
            )
            query = q.interface_query[
                        'display_product_cart'] + str(self.from_user.id)
            response = db.execution_of_requests(connection, query)
            cart = sorted(list(set(response)))
            index_str = extract_id(self.data)
            index = int(index_str[1])
            product_id = cart[index][0]
            query = q.interface_query['cart_id_info'] + str(self.from_user.id)
            cart_id = db.execution_of_requests(connection, query)
            query = q.interface_query['add_product_cart']
            data = (cart_id[0][0], product_id)
            db.execution_of_requests(connection, query, data)
            connection.close()
            InterfaceInteraction.cart(self)
            InterfaceInteraction.alert(self, "Товар добавлен в корзину")
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return

    def remove_product(self):
        try:
            connection = db.create_connection(
                "merch_telegram_bot_db", "postgres", "Qsf98%x$",
                "127.0.0.1",
                "5432"
            )
            query = q.interface_query[
                        'display_product_cart'] + str(self.from_user.id)
            response = db.execution_of_requests(connection, query)
            cart = sorted(list(set(response)))
            index_str = extract_id(self.data)
            index = int(index_str[1])
            product_id = cart[index][0]
            query = q.interface_query['cart_id_info'] + str(self.from_user.id)
            response = db.execution_of_requests(connection, query)
            cart_id = response[0][0]
            query = f"""DELETE FROM cart_product WHERE ctid IN(SELECT ctid 
            FROM cart_product WHERE cart_id={cart_id} AND 
            product_id={product_id} LIMIT 1)"""
            db.execution_of_requests(connection, query)
            connection.close()
            InterfaceInteraction.cart(self)
            InterfaceInteraction.alert(self, "Товар убран из корзины.")
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return

    def callback_data_handler(self):
        try:
            connection = db.create_connection(
                "merch_telegram_bot_db", "postgres", "Qsf98%x$", "127.0.0.1",
                "5432"
            )
            id_element = extract_id(self.data)
            if id_element[0] == 'cat':
                query = q.interface_query['product'] + id_element[1]
                product = db.execution_of_requests(connection, query)
                bot.edit_message_text(chat_id=self.message.chat.id,
                                      message_id=self.message.message_id,
                                      text=f'{product[0][0]}')
                if not product[0][1]:
                    bot.send_message(self.message.chat.id,
                                     "Товары отсутствуют 😔")
                elif not product[0][5]:
                    bot.send_message(self.message.chat.id,
                                     "Фотографии товаров отсутствуют 😔")
                else:
                    for i in product:
                        show_product_keyboard = key.show_product(i)
                        bot.send_photo(self.from_user.id, i[5],
                                       caption=f'\n{i[2]}\n{i[3]}',
                                       reply_markup=show_product_keyboard)
                connection.close()
                bot.answer_callback_query(self.id, show_alert=False)
            elif id_element[0] == 'prod':
                query = q.interface_query['cart_id_info'] + \
                        str(self.from_user.id)
                cart_id = db.execution_of_requests(connection, query)
                query = q.interface_query['add_product_cart']
                data = (cart_id[0][0], id_element[1])
                db.execution_of_requests(connection, query, data)
                InterfaceInteraction.alert(self, "Товар добавлен в корзину")
            elif id_element[0] == 'delete':
                InterfaceInteraction.delete_product(self)
            elif id_element[0] == 'remove':
                InterfaceInteraction.remove_product(self)
            elif id_element[0] == 'add':
                InterfaceInteraction.add_product(self)
            elif id_element[0] == 'prev':
                InterfaceInteraction.cart(self)
            elif id_element[0] == 'next':
                InterfaceInteraction.cart(self)
            elif id_element[0] == 'order':
                pass
            elif id_element[0] == 'continue':
                pass
            else:
                pass
            InterfaceInteraction.alert(self)
            connection.close()
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return


def extract_id(data):
    element = data.split('_')
    return element
