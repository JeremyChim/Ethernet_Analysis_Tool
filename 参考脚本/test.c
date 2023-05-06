#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include "test.h"
#include <time.h> /*related to tm struct */
#include <sys/time.h>
#include <arpa/inet.h>
#include <net/if.h>

#define BUF_SIZE 1024u

#define UDP_DATA_OFFSET 42u

#define UDP_MSG_17F 0x17F
#define UDP_MSG_31B 0x31B
#define UDP_MSG_146 0x146
#define UDP_MSG_232 0x232//GGA
#define UDP_MSG_233 0x233//GSA 
#define UDP_MSG_234 0x234//GSV 

#define UDP_SIGNAL_146_LEN 41u
#define UDP_SIGNAL_31B_LEN 28u
#define UDP_SIGNAL_17F_LEN 31u

#define CRC32_POLYNOMIAL     0xF4ACFB13U//70A122
#define CRC32_START_VALUE    0xFFFFFFFFU
#define CRC32_XOR            0xFFFFFFFFU


//20221120
//1.修改msgDespInfo_t结构体的factor和result类型从float改为double，解决经纬度精度只到小数点后6位的问题。

//20221209
//1.修改146的角速度和角速度零偏的factor值从0.000017456改为0.000017452
//2.修改146的角速度零偏的最小值从-0.1743改为-0.17452
//3.修改17F轮速的factor从0.05625改为0.015625。

//20221215
//1.增加GGA和GSA的数据解析。
//2.屏蔽一些无效数据的打印，减少日志的打印内容。


msgDespInfo_t msgDespInfo_146[UDP_SIGNAL_146_LEN] = 
{
	{"INS_Vehicle_X_Acc",3,0,0.001,-40,0},
	{"INS_Vehicle_X_Rate",3,0,0.000017452,-4.363,0},
	{"INS_Vehicle_Y_Acc",3,0,0.001,-40,0},
	{"INS_Vehicle_Y_Rate",3,0,0.000017452,-4.363,0},
	{"INS_Vehicle_Z_Acc",3,0,0.001,-40,0},
	{"INS_Vehicle_Z_Rate",3,0,0.000017452,-4.363,0},
	{"INS_IMU_Time",4,0,1,0,0},
	{"INS_IMU_Valid",1,0,1,0,0},
	{"INS_IMU_X_Acc_Bias",2,0,0.001,-10,0},
	{"INS_IMU_X_Rate_Bias",2,0,0.000017452,-0.17452,0},
	{"INS_IMU_Y_Acc_Bias",2,0,0.001,-10,0},
	{"INS_IMU_Y_Rate_Bias",2,0,0.000017452,-0.17452,0},
	{"INS_IMU_Z_Acc_Bias",2,0,0.001,-10,0},
	{"INS_IMU_Z_Rate_Bias",2,0,0.000017452,-0.17452,0},
	{"INS_Vehicle_Quaternion_W",3,0,0.000001,-1,0},
	{"INS_Vehicle_Quaternion_X",3,0,0.000001,-1,0},
	{"INS_Vehicle_Quaternion_Y",3,0,0.000001,-1,0},
	{"INS_Vehicle_Quaternion_Z",3,0,0.000001,-1,0},
	{"IMU_to_Vehicle_Offset_X",3,0,0.0001,-5,0},
	{"IMU_to_Vehicle_Offset_Y",3,0,0.0001,-5,0},
	{"IMU_to_Vehicle_Offset_Z",3,0,0.0001,-5,0},
	{"146_INS_Timestamp",8,0,0.0001,0,0},
	{"INS_Timestamp_Valid",1,0,1,0,0},
	{"INS_146_TiDiffer",2,0,1,0,0},
	{"INS_IMU_X_Acc",3,0,0.001,-40,0},
	{"INS_IMU_X_Rate",3,0,0.000017452,-4.363,0},
	{"INS_IMU_Y_Acc",3,0,0.001,-40,0},
	{"INS_IMU_Y_Rate",3,0,0.000017452,-4.363,0},
	{"INS_IMU_Z_Acc",3,0,0.001,-40,0},
	{"INS_IMU_Z_Rate",3,0,0.000017452,-4.363,0},
	{"IMU_to_Vehicle_Error_Quaternion_W",3,0,0.000001,-1,0},
	{"IMU_to_Vehicle_Error_Quaternion_X",3,0,0.000001,-1,0},
	{"IMU_to_Vehicle_Error_Quaternion_Y",3,0,0.000001,-1,0},
	{"IMU_to_Vehicle_Error_Quaternion_Z",3,0,0.000001,-1,0},

    {"SlowDr_Status",1,0,1,0,0},
	{"INS_Vehicle_SlowDr_Pos_X",4,0,0.001,-2147483.647,0},//offset is not set
	{"INS_Vehicle_SlowDr_Pos_Y",4,0,0.001,-2147483.647,0},//offset is not set
	{"INS_Vehicle_SlowDr_Pos_Z",4,0,0.001,-2147483.647,0},//offset is not set
	{"INS_Vehicle_SlowDr_Roll",3,0,0.001,-90,0},
    {"INS_Vehicle_SlowDr_Pitch",3,0,0.001,-180,0},
    {"INS_Vehicle_SlowDr_Heading",3,0,0.001,0,0},

};

msgDespInfo_t msgDespInfo_31B[UDP_SIGNAL_31B_LEN] =
{
	{"INS_GNSS_Time_Year",2,0,1,2000,0},
	{"INS_GNSS_Time_Month",1,0,1,0,0},
	{"INS_GNSS_Time_Date",1,0,1,0,0},
	{"INS_GNSS_Time_Hour",1,0,1,0,0},
	{"INS_GNSS_Time_Minute",1,0,1,0,0},
	{"INS_GNSS_Time_Second",1,0,1,0,0},
	{"INS_GNSS_Time_mSecond",2,0,1,0,0},
	{"GNSS_Speed",3,0,0.001,-100,0},
	{"GNSS_Speed_Err",2,0,1,0,0},
	{"INS_GNSS_Speed_North",3,0,0.001,-100,0},
	{"INS_GNSS_Speed_East",3,0,0.001,-100,0},
	{"INS_GNSS_Speed_Earth",3,0,0.001,-100,0},
	{"INS_GNSS_Speed_North_Err",2,0,1,0,0},
	{"INS_GNSS_Speed_East_Err",2,0,1,0,0},
	{"INS_GNSS_Speed_Earth_Err",2,0,1,0,0},
	{"INS_GNSS_Difference_delay",3,0,0.001,0,0},
	{"INS_GNSS_GDOP",3,0,0.01,0,0},
	{"INS_GNSS_PDOP",3,0,0.01,0,0},
	{"INS_GNSS_HDOP",3,0,0.01,0,0},
	{"INS_GNSS_VDOP",3,0,0.01,0,0},
	{"INS_GNSS_TDOP",3,0,0.01,0,0},
	{"INS_GNSS_Speed_East_Confidence",1,0,1,0,0},
	{"INS_GNSS_Speed_North_Confidence",1,0,1,0,0},
	{"INS_GNSS_Speed_Earth_Confidence",1,0,1,0,0},
	{"INS_WatchedSV",1,0,1,0,0},
	{"INS_UsedSV",1,0,1,0,0},
	{"INS_GPS_Flight_Path_Angle",3,0,0.001,-180,0},
	{"INS_GNSS_Time_Valid",1,0,1,0,0}
};

msgDespInfo_t msgDespInfo_17F[UDP_SIGNAL_17F_LEN] = 
{
	{"INS_Current_Pos_Heading",3,0,0.001,0,0},
	{"INS_Current_Pos_Heading_Accuracy",2,0,0.001,0,0},
	{"INS_Current_Pos_Heading_Confidence",1,0,1,0,0},
	{"INS_Current_Pos_Height_Confidence",1,0,1,0,0},
	{"INS_Current_Pos_Lat_Confidence",1,0,1,0,0},
	{"INS_Vehicle_Lat",4,0,0.0000001,-90,0},
	{"INS_Current_Pos_Lat_GNSS_Err",2,0,1,0,0},
	{"INS_Current_Pos_Long_Confidence",1,0,1,0,0},
	{"INS_Vehicle_Lon",4,0,0.0000001,-180,0},
	{"INS_Current_Pos_Long_GNSS_Err",2,0,1,0,0},
	{"INS_Current_Pos_Pitch",3,0,0.001,-180,0},
	{"INS_Current_Pos_Pitch_Accuracy",2,0,0.001,0,0},
	{"INS_Current_Pos_Pitch_Confidence",1,0,1,0,0},
	{"INS_Current_Pos_Roll",3,0,0.001,-90,0},
	{"INS_Current_Pos_Roll_Accuracy",2,0,0.001,0,0},
	{"INS_Current_Pos_Roll_Confidence",1,0,1,0,0},
	{"INS_GNSS_Height",3,0,0.001,-1000,0},
	{"INS_GNSS_Height_Err",2,0,1,0,0},
	{"INS_GNSS_Mode",1,0,1,0,0},
	{"FL_wheel_vel",2,0,0.015625,-100,0},
	{"FR_wheel_vel",2,0,0.015625,-100,0},
	{"RL_wheel_vel",2,0,0.015625,-100,0},
	{"RR_wheel_vel",2,0,0.015625,-100,0},
	{"RL_wheel_factor",2,0,0.0001,0,0},
	{"RR_wheel_factor",2,0,0.0001,0,0},
	{"INS_GPS_Week",2,0,1,0,0},
	{"INS_GPS_Time",4,0,1,0,0},
	{"17F_INS_Timestamp",8,0,0.0001,0,0},
	{"INS_Timestamp_Valid",1,0,1,0,0},
	{"INS_POS_Match_RTK_POS_Mark",1,0,1,0,0},
	{"INS_17F_TiDiffer",2,0,1,0,0}	
};

void PrintTime(void)
{
	 time_t now;   
	 struct tm *timenow;   
	 char strtemp[255];   
	   
	 time(&now);   
	 timenow = localtime(&now);   
	 printf("Time:%s", asctime(timenow)); 
}
static uint32 reflectResult(uint32 data)
{
    uint32 reflection = 0x00000000U;
    uint8 bit;
    uint32 tmpData = data;

    for (bit = 0; bit < 32; bit++) {

        /* Set reflection  */
        if ((tmpData & 0x01U) != 0) {
            reflection |= (1UL << (31UL - bit));
        }

        tmpData = tmpData >> 1;
    }

    return reflection;

}


/* Reflects the indata bit by bit */
static uint8 reflectInData(uint8 data)
{
    uint8 reflection = 0x00;
    uint8 bit;
    uint32 tmpData = data;

    for (bit = 0; bit < 8; bit++) {

        if ((tmpData & 0x01U) != 0) {
            /*lint -e{734} Lint exception:  False warning since bit <= 7 */
            reflection |= (1U << (7U-bit));
        }

        tmpData = (tmpData >> 1U);
    }

    return reflection;

}


static uint32 CalculateCRC32(const uint8* message, uint32 nBytes, uint32 start)
{
    uint32 remainder = reflectResult(start);
    uint8  bit;
    const uint32  topbit = 0x80000000U;

    /* Perform modulo-2 division, a byte at a time. */
    for (uint32 byte = 0; byte < nBytes; byte++) {
        /* Bring the next byte into the remainder. */
        uint32 reflectedData = reflectInData(*message);
        remainder ^= (reflectedData << 24u);
        message++;

        /* Perform modulo-2 division, a bit at a time. */
        for (bit = 8; bit > 0; bit--) {

            /* Try to divide the current data bit. */
            if ((remainder & topbit) != 0) {
                remainder = (remainder << 1u) ^ CRC32_POLYNOMIAL;
            }
            else {
                remainder = (remainder << 1u);
            }
        }
    }

    return reflectResult(remainder);
}


/* @req SWS_CRC_00003 */
/* @req SWS_CRC_00016 */
/* @req SWS_CRC_00020 */
/* @req SWS_CRC_00055 */
uint32 Crc_CalculateCRC32( const uint8* Crc_DataPtr, uint32 Crc_Length, uint32 Crc_StartValue32, boolean Crc_IsFirstCall ) 
{

    uint32 crc = 0; /* Default return value if NULL pointer */

    if (Crc_DataPtr != NULL) {

        crc = (1 == Crc_IsFirstCall) ? CRC32_START_VALUE : (Crc_StartValue32 ^ CRC32_XOR);


        crc = CalculateCRC32(Crc_DataPtr, Crc_Length, crc);

        crc = crc ^ CRC32_XOR;
    }

    return crc;
}






void littleToBigBuf(uint8* lBuff, uint8* bBuff, uint16 len)
{
    uint16 i = 0;

    for(i = 0; i < len; i++)
    {
        bBuff[len-1-i] = lBuff[i];
    }
}

void buff2SignalHandle(msgDespInfo_t * msgDespInfo,uint16 len,uint8*buff)
{
//	printf("buff2SignalHandle\n");
	uint16 offset = 0;
	uint16 i = 0;

	for(i = 0; i < len; i++)
	{
		msgDespInfo[i].value = 0;
		for (int j = 0; j < msgDespInfo[i].byteLenth; ++j) 
		{
			msgDespInfo[i].value = msgDespInfo[i].value<<8 | buff[offset+j];
		}
		offset += msgDespInfo[i].byteLenth;

		msgDespInfo[i].result = msgDespInfo[i].value * msgDespInfo[i].factor + msgDespInfo[i].offset;
        //if(strcmp(msgDespInfo[i].desp, "146_INS_TiStamp")==0 || strcmp(msgDespInfo[i].desp, "17F_INS_TiStamp")==0||strcmp(msgDespInfo[i].desp, "INS_GPS_Time")==0)
		{
		  
		   printf("%s value:%ld 0x%lx result:%.8f\n",msgDespInfo[i].desp,msgDespInfo[i].value,msgDespInfo[i].value,msgDespInfo[i].result);
		}
	}
	printf("\n");
}



_c_Enet_INS_Tx_146_buf_u c_Enet_INS_Tx_146_buf = {0};
_c_Enet_INS_Tx_17F_buf c_Enet_INS_Tx_17F_buf = {0};
_c_Enet_INS_Tx_31B_buf c_Enet_INS_Tx_31B_buf = {0};
_c_Enet_INS_Tx_232_buf c_Enet_INS_Tx_232_buf = {0};
_c_Enet_INS_Tx_233_buf c_Enet_INS_Tx_233_buf = {0};
_c_Enet_INS_Tx_234_buf c_Enet_INS_Tx_234_buf = {0};

uint8 receiveBuffHandle(uint8*readBuff, uint16 len)
{
    uint8 buff[1024];
    udpHead_u udpHead;
    uint16 index = 0;
	uint32 type = 0;
	uint32 crc = 0;
	uint32 recieve_crc;
	uint16 DataLen = 0;
	
    memset(buff, 0x00, sizeof(buff));
    memset(udpHead.head_buff, 0x00, sizeof(udpHead));
  
	for(uint8_t i = 0; i<20; i++)
	{
		udpHead.head_buff[i] = readBuff[i];
	}

    index += sizeof(udpHead);   
	littleToBigBuf((uint8*)&udpHead.udpHead_t.message_type,(uint8*)&type,sizeof(type));
//	printf("Rx ID=%02x\n",type);

	crc = Crc_CalculateCRC32( &readBuff[index], len-index, 0, 1 );
	littleToBigBuf((uint8*)&udpHead.udpHead_t.crc_value,(uint8*)&recieve_crc,sizeof(recieve_crc));
//	printf("CRC_LOCAL_CALCULATE::%02x CRC_RECEIVED::%02x    ",crc,recieve_crc);
	if(crc == recieve_crc)
	{
//		printf("CRC Check Success!!\n");
	}
	else
	{
		printf("CRC Check Fail!!!give up this package!\n");
		return 0;
	}
//	cnt=readBuff[2]<<8+readBuff[3];
//	printf("cnt:%d \n",cnt);
	switch(type)
	{
#if 1
	case UDP_MSG_146:
		printf("MSG_146\n");
		memcpy(c_Enet_INS_Tx_146_buf._c,&readBuff[index],sizeof(c_Enet_INS_Tx_146_buf));
		buff2SignalHandle(msgDespInfo_146,UDP_SIGNAL_146_LEN,c_Enet_INS_Tx_146_buf._c);
		break;

	case UDP_MSG_17F:
		printf("MSG_17F\n");
		memcpy(c_Enet_INS_Tx_17F_buf._c,&readBuff[index],sizeof(c_Enet_INS_Tx_17F_buf));
		buff2SignalHandle(msgDespInfo_17F,UDP_SIGNAL_17F_LEN,c_Enet_INS_Tx_17F_buf._c);
		break;
#endif
	case UDP_MSG_31B:
		printf("MSG_31B\n");
		memcpy(c_Enet_INS_Tx_31B_buf._c,&readBuff[index],sizeof(c_Enet_INS_Tx_31B_buf));
		buff2SignalHandle(msgDespInfo_31B,UDP_SIGNAL_31B_LEN,c_Enet_INS_Tx_31B_buf._c);
		break;
#if 1
	case UDP_MSG_232:
		printf("MSG_232\n");
		PrintTime();
		littleToBigBuf(&readBuff[index],(uint8*)&DataLen,sizeof(DataLen));
		printf("GGA size:%d,dataLen:%d\n",(len-index),DataLen);
		memcpy(c_Enet_INS_Tx_232_buf._c,&readBuff[index],sizeof(c_Enet_INS_Tx_232_buf));
		printf("GGA:%s",&c_Enet_INS_Tx_232_buf._c[INS_ETH_DATA_LENGH_BYTE]);
		printf("\n");
		printf("\n");
		break;
		
	case UDP_MSG_233:
		printf("MSG_233\n");
//		PrintTime();
		littleToBigBuf(&readBuff[index],(uint8*)&DataLen,sizeof(DataLen));
		printf("GSA size:%d,dataLen:%d\n",(len-index),DataLen);
		memcpy(c_Enet_INS_Tx_233_buf._c,&readBuff[index],sizeof(c_Enet_INS_Tx_233_buf));
	    printf("GSA:%s",&c_Enet_INS_Tx_233_buf._c[INS_ETH_DATA_LENGH_BYTE]);
		printf("\n");
		printf("\n");
		break;
		
	case UDP_MSG_234:
		printf("MSG_234\n");
//		PrintTime();
		littleToBigBuf(&readBuff[index],(uint8*)&DataLen,sizeof(DataLen));
		printf("GSV size:%d,dataLen:%d\n",(len-index),DataLen);
		memcpy(c_Enet_INS_Tx_234_buf._c,&readBuff[index],sizeof(c_Enet_INS_Tx_234_buf));
		printf("GSA:%s",&c_Enet_INS_Tx_234_buf._c[INS_ETH_DATA_LENGH_BYTE]);
		printf("\n");
		printf("\n");
		break;		
#endif
	default:
		break;
	}
  
}




void ServerDataHandle_recvform_sendto(int fd)
{
	int byte = 0, cnt = 0;
	uint8_t buf[BUF_SIZE] = {0};
	socklen_t len = sizeof(struct sockaddr_in);
	struct sockaddr_in clientaddr;
	
	if(fd <= 0) 
	{
		perror("socket fd value err");
		return ;
	}
	
	while(1)
	{
		byte = recvfrom(fd, buf, BUF_SIZE, 0, (struct sockaddr *)&clientaddr, &len);	//\B6\C1ȡclient\CA\FD\BE\DD,\D3\D0\CA\FD\BEݸ\FC\D0²Ŷ\C1ȡ\A3\AC\B7\F1\D4\F2\D7\E8\C8\FB

		if(byte == 0)							//\BFͻ\A7\B6˹ر\D5ʱ\A3\AC\B6\C1ȡ\CA\FD\BEݸ\F6\CA\FDΪ0
		{
			printf("sockfd:%d read over\n", fd);
			break;
		}
		if(byte < 0)
		{
			perror("read failed");	
			break;
		}
#if 0
		printf("client IP:%s, port:%d, datalen:%d, info:", inet_ntoa(clientaddr.sin_addr), clientaddr.sin_port, byte);
		for(int i = 0; i < byte; i++)
		{
			printf("%02x",buf[i]);
		}
		printf("\n");
#endif

		receiveBuffHandle(buf, byte);
		//sprintf(buf, "server send cnt:%d\n", ++cnt);
		//sendto(fd, buf, strlen(buf), 0, (struct sockaddr *)&clientaddr, sizeof(clientaddr));
		//usleep(10000);
	}
	close(fd);
	
}

int main(int argc, void *argv[] )
{
	int listenfd, opt = 1;
	struct sockaddr_in serveraddr;

	listenfd = socket(AF_INET, SOCK_DGRAM, 0);
	printf("Creat Socket listenfd:%d\n",listenfd);
	if(listenfd < 0)
	{
		perror("Create socket fail.");
		return -1;
	}	
	
    memset( (void*)&serveraddr,0,sizeof(struct sockaddr_in) );
    serveraddr.sin_family 		= AF_INET;
	serveraddr.sin_port			= htons(51001);
	serveraddr.sin_addr.s_addr 	= inet_addr("172.16.6.34");
	serveraddr.sin_addr.s_addr 	= htonl(INADDR_ANY);

#if 1
	struct ip_mreqn group; /*组播结构体*/
	inet_pton(AF_INET, "225.0.6.21", &group.imr_multiaddr); /* 设置组播组地址*/
	inet_pton(AF_INET, "0.0.0.0", &group.imr_address);      /*使用本地任意IP添加到组播组*/
	
	char *net_name = argv[1];
	printf("net_name = %s\n", net_name);
	group.imr_ifindex = if_nametoindex(net_name);  /* 多网卡时，需要设置指定网卡名 编号 ip ad */
#else
	struct ip_mreq group;
	group.imr_multiaddr.s_addr = inet_addr("225.0.6.21");
	group.imr_interface.s_addr = htonl(INADDR_ANY);
#endif
	setsockopt(listenfd, IPPROTO_IP, IP_ADD_MEMBERSHIP, &group, sizeof(group)); /* 将client加入组播组*/

	if(bind(listenfd, (struct sockaddr *)&serveraddr, sizeof(struct sockaddr_in))<0)	//\B0\F3\B6\A8
	{
		perror("bind error.");
		return -1;
	}
	printf("Start Receive data\n");
	ServerDataHandle_recvform_sendto(listenfd);
	
	return 0;
}
