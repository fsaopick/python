from functools import reduce

class OrderSystem:
    def __init__(self, computer_club):
        self._computer_club = computer_club
        self._korzina = []

    def dobavit_v_korzinu(self, nazvanie):
        produkt = next((item for item in self._computer_club.produkty if item["nazvanie"] == nazvanie), None)

        if produkt:
            self._korzina.append(produkt)
            print(f"{nazvanie} добавлен в корзину.")
        else:
            print("Продукт не найден.")

    def rasschitat_itog(self):
        return reduce(lambda itog, item: itog + item["cena"], self._korzina, 0)

    def sozdat_zakaz(self, nomer_zala, chasy):
        if 0 <= nomer_zala < len(self._computer_club.zaly):

            stoimost_zala = self._computer_club.zaly[nomer_zala]['cena'] * chasy
            stoimost_korziny = self.rasschitat_itog()
            obshaya_stoimost = stoimost_zala + stoimost_korziny

            print("\nДетали заказа:")
            print(f"Аренда зала: {stoimost_zala} руб.")
            print(f"Продукты в корзине: {stoimost_korziny} руб.")
            print(f"Общая стоимость заказа: {obshaya_stoimost} руб.")
            
        else:
            print("Некорректный номер зала.")

    def pokazat_korzinu(self):
        if not self._korzina:
            print("Корзина пуста.")
        else:
            print("\nВаша корзина:")
            for idx, produkt in enumerate(self._korzina):
                print(f"{idx + 1}. {produkt['nazvanie']} - {produkt['cena']} руб.")
            print(f"Общая стоимость корзины: {self.rasschitat_itog()} руб.")