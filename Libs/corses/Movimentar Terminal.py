import os
import curses

def main(stdscr):
    # Configuração inicial do curses
    stdscr.nodelay(1)  # Modo de não bloqueio
    stdscr.timeout(100)  # Tempo limite de 100ms para entrada
    for i in range(10):
        stdscr.addstr(i, 0, f"Texto de exemplo {i}")
    stdscr.refresh()  # Atualize a janela para exibir o texto

    # Obtém a altura (número de linhas) e largura (número de colunas) da janela
    height, width = stdscr.getmaxyx()

    while True:
        key = stdscr.getch()
        if key != -1:
            if key == curses.KEY_UP:
                # Seta para cima pressionada
                if curses.getsyx()[0] > 0:
                    stdscr.move(curses.getsyx()[0] - 1, curses.getsyx()[1])
            elif key == curses.KEY_DOWN:
                # Seta para baixo pressionada
                if curses.getsyx()[0] < height - 1:
                    stdscr.move(curses.getsyx()[0] + 1 , curses.getsyx()[1])
            elif key == curses.KEY_LEFT:
                # Seta para a esquerda pressionada
                if curses.getsyx()[1] > 0:
                    stdscr.move(curses.getsyx()[0], curses.getsyx()[1] - 1)
            elif key == curses.KEY_RIGHT:
                # Seta para a direita pressionada
                if curses.getsyx()[1] < width - 1:
                    stdscr.move(curses.getsyx()[0], curses.getsyx()[1] + 1)
        stdscr.refresh()
curses.wrapper(main)  # Inicializa o curses e chama a função main

input()
os.system("pause")
