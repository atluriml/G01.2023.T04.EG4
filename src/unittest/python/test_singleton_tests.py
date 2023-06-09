"""Singleton Tests Module"""
from unittest import TestCase

from uc3m_logistics import OrderManager
from uc3m_logistics.stores import OrderShippingStore
from uc3m_logistics.stores.order_delivery_store import OrderDeliveryStore
from uc3m_logistics.stores.order_request_store import OrderRequestStore


class SingletonTests(TestCase):
    """Singleton Tests Class"""

    def test_order_manager_is_singleton_test(self):
        """test_order_manager_is_singleton_test function"""
        order_manager_1 = OrderManager()
        order_manager_2 = OrderManager()
        self.assertEqual(id(order_manager_1), id(order_manager_2))

    def test_order_request_store_is_singleton_test(self):
        """test_order_request_store_is_singleton_test function"""
        order_request_store_1 = OrderRequestStore()
        order_request_store_2 = OrderRequestStore()
        self.assertEqual(id(order_request_store_1), id(order_request_store_2))

    def test_order_shipping_store_is_singleton_test(self):
        """test_order_shipping_store_is_singleton_test function"""
        order_shipping_store_1 = OrderShippingStore()
        order_shipping_store_2 = OrderShippingStore()
        self.assertEqual(id(order_shipping_store_1), id(order_shipping_store_2))

    def test_order_delivery_store_is_singleton_test(self):
        """test_order_delivery_store_is_singleton_test function"""
        order_delivery_store_1 = OrderDeliveryStore()
        order_delivery_store_2 = OrderDeliveryStore()
        self.assertEqual(id(order_delivery_store_1), id(order_delivery_store_2))
