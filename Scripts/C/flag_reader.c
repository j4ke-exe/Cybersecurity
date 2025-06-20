#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>

void print_the_flag() {
  int fd = open("/tmp/flag", O_RDONLY);
  if (fd == -1) {
    perror("open");
    return;
  }

  struct stat st;
  if (fstat(fd, &st) == -1) {
    perror("fstat");
    close(fd);
    return;
  }

  off_t file_size = st.st_size;
  char *buffer = malloc(file_size + 1);
  if (!buffer) {
    perror("malloc");
    close(fd);
    return;
  }

  ssize_t bytesRead = read(fd, buffer, file_size);
  if (bytesRead == -1) {
    perror("read");
    free(buffer);
    close(fd);
    return;
  }

  buffer[bytesRead] = '\0';
  printf("%s\n", buffer);

  free(buffer);
  close(fd);
}
