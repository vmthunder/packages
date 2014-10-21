#!/usr/bin/env bash

LOOP_NUM=15    #default=64; >=8,<=128
CACHE_SIZE=1k
SNAP_SIZE=512
#IMAGE_FILE_NUM=3
#IMAGE_FILE_SIZE=512

mkdir -p /root/blocks

echo "creating a cache device for this computer node ..."
dd if=/dev/zero of=/root/blocks/cache.blk bs=1M count=$CACHE_SIZE
losetup -d /dev/loop0
losetup /dev/loop0 /root/blocks/cache.blk
echo "create the cache device completed!"

echo "creating snapshot devices ..."
modprobe loop max_loop=$LOOP_NUM
for i in $(seq 8 $(($LOOP_NUM-1))); do
    mknod -m 660 /dev/loop$i b 7 $i
done
for i in $(seq 1 $LOOP_NUM); do
    dd if=/dev/zero of=/root/blocks/snapshot$i.blk bs=1M count=$SNAP_SIZE
done
echo "create snapshot devices completed!"

:<<note
echo "creating image files for test on this image server ..."
for i in $(seq 1 $IMAGE_FILE_NUM); do
    dd if=/dev/zero of=/root/blocks/image$i.blk bs=1M count=$IMAGE_FILE_SIZE
done
echo "create image files completed!"
note
