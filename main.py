import random, math, pygame, threading;

slots = []

highlighted = -1

running = False

endThreads = False

lock = threading.Lock()

###############################################################################
#                                  CLASSES                                    #
###############################################################################
class Slot:
    y = 0



###############################################################################
#                                 FUNCTIONS                                   #
###############################################################################

def thread_task(lock,screen, running):
    state = 0
    i = 0
    sorted = True
    finished = False
    while True:
        #lock.acquire()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                break
        
        if running == False:
            break

        highlight = 0
        if state == 0:
            s = Slot()
            s.y = random.randint(0,255)
            highlight = i
            slots.append(s)
            if i >= 255:
                state = 1
                i = 0
        elif i < len(slots) - 1:
            if i >= 255:
                sorted = True
                i = 0
            if slots[i].y > slots[i + 1].y:
                highlight = i
                print(str(slots[i].y) + " <-> " + str(slots[i + 1].y))
                y = slots[i].y
                slots[i].y = slots[i + 1].y
                slots[i + 1].y = y
                sorted = False
        
        screen.fill((0,0,0))

        for j in range(len(slots)):
            color = 0
            if i == j or (sorted == True and j <= i):
                color = (255,0,0)
            else:
                color = (255,255,255)
            
            pygame.draw.rect(screen, color,(j*2, 512 - slots[j].y*2, 2,slots[j].y*2))
        
        if sorted and i == 255:
            finished = True

        pygame.display.update()
        #pygame.time.wait(1)
        if finished == False:
            i += 1
        else:
            i = 0
        if i >= 256:
            i = 0
            sorted = True
        #print(i)
        #lock.release()
    #endThreads = True

#def thread_task2(screen, running):
#    while True:


###############################################################################
#                                   INIT                                      #
###############################################################################
pygame.init()

threads = []

screen = pygame.display.set_mode((512,512))

running = True

#for i in range(1024):
#    t = threading.Thread(target=thread_task,args=[lock,screen,running])
#    t.start()
#    print(i)
#    threads.append(t)

thread_task(lock,screen,running)

#t = threading.Thread(target=thread_task2,args=[screen,running])

#for t in threads:
#        t.join()

#t.start()
#t.join()