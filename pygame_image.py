import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#練習１
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習７-１
    kk_img = pg.image.load("fig/3.png")#練習２
    kk_img = pg.transform.flip(kk_img, True, False)#練習２
    kk_img_rct = kk_img.get_rect()#練習８
    kk_img_rct.center = 300,200#練習８
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)#練習２

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_img_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            kk_img_rct.move_ip((0,+1))
        if key_lst[pg.K_LEFT]:
            kk_img_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            kk_img_rct.move_ip((+1,0))

        x = tmr%3200 
        screen.blit(bg_img, [-x, 0])#練習６
        screen.blit(bg_img2, [-x+1600, 0])#練習７-１
        screen.blit(bg_img, [-x+3200, 0])#練習７-２
        screen.blit(bg_img2, [-x+4800, 0])#練習７-２
        screen.blit(kk_img, [300, 200])#練習４

        #screen.blit(kk_img,kk_img_rct)#練習８
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()