SNIPER_BASE_DIR ?= /home/mary/advcomparch_ex4/sniper-7.3
SNIPER_INCLUDE_DIR = $(SNIPER_BASE_DIR)/include

CC = gcc

TARGET = locks 

LFLAG ?= -DMUTEX 
IMPLFLAG ?= -DREAL ## -DSNIPER or -DREAL 

CFLAGS ?= -Wall -O0 -lpthread $(IMPLFLAG) $(LFLAG) #-DDEBUG
CFLAGS += -I$(SNIPER_INCLUDE_DIR)
CFLAGS += -Wno-unused-variable

$(TARGET): locks_scalability.c
	$(CC) $^ $(HOOKS_LDFLAGS) $(CFLAGS) -o $@

clean :
	rm -f $(TARGET)
