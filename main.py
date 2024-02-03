import sys
from geocoder import get_ll_span
from mapapi_PG import show_map
import requests
import pygame
pygame.init()
# пока не доделана скинул чтобы дома продолжить

def main1(toponym_to_find='Тольятти, Автозаводский Район', delt=2):
    if toponym_to_find:
        ll, spn = get_ll_span(toponym_to_find, delt)
        add_params = f"pt={ll}"
        ll_span = f'll={ll}&spn={spn}'
        show_map(ll_spn=ll_span, map_type="map", delta=delt)

    else:
        print('No toponym')
    print(delt)

#def main2():

