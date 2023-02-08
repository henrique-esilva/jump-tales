import pygame, sys
from pygame.locals import *

#  pegar o valor de retorno com
#  uma VAR, ok?
def import_animation(arg, start = 0):     # O "arg"(parametro) deve ser o nome do diretório + "\\" + nome da animação. E PRONTO. O subprograma faz o resto
    a = []

    for i in range ( start , 999 ):
        try:


            patch = arg + ("\\frame%04d.png" % i)      # Aqui é criada uma string do caminho da imagem


            a.append(          pygame.image.load( patch )          )    # Aqui a imagem é importada

        except:    break

    if len(a) == 0:

        print('\nWARNING: \'import_animation()\' retornando vetor de 0 (zero) valores')
        print('    a animação não está recebendo nenhum quadro!')
    return a