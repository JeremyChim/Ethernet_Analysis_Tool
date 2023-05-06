#ifndef UDP_SERVER_H
#define UDP_SERVER_H

#include <stdio.h>





typedef unsigned char boolean;         /** \brief Autosar boolean type */

typedef signed char sint8;             /** \brief 8-bit signed integer */
typedef unsigned char uint8;           /** \brief 8-bit unsigned integer */
typedef signed short sint16;           /** \brief 16-bit signed integer */
typedef unsigned short uint16;         /** \brief 16-bit unsigned integer */
typedef signed int sint32;            /** \brief 32-bit signed integer */
typedef unsigned int uint32;          /** \brief 32-bit unsigned integer */

/* Deviation from MISRA-C:2004 rule 1.1 and QA-C message 1027, MISRA-C:2012 Dir-1.1.
   Justification: 64bit is supported by the long long in ARM. */
/* PRQA S 1027 2 */
typedef signed long  sint64;       /** \brief 64-bit signed integer */
typedef unsigned long  uint64;     /** \brief 64-bit unsigned integer */

typedef unsigned long uint8_least;     /** \brief fast 8-bit unsigned integer */
typedef unsigned short uint16_least;   /** \brief fast 16-bit unsigned integer */
typedef unsigned long uint32_least;    /** \brief fast 32-bit unsigned integer */
                                       
typedef signed long sint8_least;       /** \brief fast 8-bit signed integer */
typedef signed short sint16_least;     /** \brief fast 16-bit signed integer */
typedef signed long sint32_least;      /** \brief fast 32-bit signed integer */


#define INS_ETH_DATA_LENGH_BYTE    2//2为数据长度lenght
#define INS_GGA_DATA_NUMS          120
#define INS_GSA_DATA_NUMS          80
#define INS_GSV_DATA_NUMS          80

#pragma pack (1)


typedef struct
{
	uint8 INS_Current_Pos_X_Accel_0;
	uint8 INS_Current_Pos_X_Accel_1;
	uint8 INS_Current_Pos_X_Accel_2;
	uint8 INS_Current_Pos_X_Rate_0;
	uint8 INS_Current_Pos_X_Rate_1;
	uint8 INS_Current_Pos_X_Rate_2;
	uint8 INS_Current_Pos_Y_Accel_0;
	uint8 INS_Current_Pos_Y_Accel_1;
	uint8 INS_Current_Pos_Y_Accel_2;
	uint8 INS_Current_Pos_Y_Rate_0;
	uint8 INS_Current_Pos_Y_Rate_1;
	uint8 INS_Current_Pos_Y_Rate_2;
	uint8 INS_Current_Pos_Z_Accel_0;
	uint8 INS_Current_Pos_Z_Accel_1;
	uint8 INS_Current_Pos_Z_Accel_2;
	uint8 INS_Current_Pos_Z_Rate_0;
	uint8 INS_Current_Pos_Z_Rate_1;
	uint8 INS_Current_Pos_Z_Rate_2;
	uint8 INS_IMU_Time_0;
	uint8 INS_IMU_Time_1;
	uint8 INS_IMU_Time_2;
	uint8 INS_IMU_Time_3;
	uint8 INS_IMU_Valid;
	uint8 INS_Pos_X_Accel_Bias_0;
	uint8 INS_Pos_X_Accel_Bias_1;
	uint8 INS_Pos_X_Rate_Bias_0;
	uint8 INS_Pos_X_Rate_Bias_1;
	uint8 INS_Pos_Y_Accel_Bias_0;
	uint8 INS_Pos_Y_Accel_Bias_1;
	uint8 INS_Pos_Y_Rate_Bias_0;
	uint8 INS_Pos_Y_Rate_Bias_1;
	uint8 INS_Pos_Z_Accel_Bias_0;
	uint8 INS_Pos_Z_Accel_Bias_1;
	uint8 INS_Pos_Z_Rate_Bias_0;
	uint8 INS_Pos_Z_Rate_Bias_1; 
	uint8 INS_Quaternion_W_0;
	uint8 INS_Quaternion_W_1;
	uint8 INS_Quaternion_W_2;
	uint8 INS_Quaternion_X_0;
	uint8 INS_Quaternion_X_1;
	uint8 INS_Quaternion_X_2;
	uint8 INS_Quaternion_Y_0;
	uint8 INS_Quaternion_Y_1;
	uint8 INS_Quaternion_Y_2;
	uint8 INS_Quaternion_Z_0;
	uint8 INS_Quaternion_Z_1;
	uint8 INS_Quaternion_Z_2;
	uint8 IMU_to_Vehicle_Offset_X_0;//47
	uint8 IMU_to_Vehicle_Offset_X_1;
	uint8 IMU_to_Vehicle_Offset_X_2;
	uint8 IMU_to_Vehicle_Offset_Y_0;
	uint8 IMU_to_Vehicle_Offset_Y_1;
	uint8 IMU_to_Vehicle_Offset_Y_2;
	uint8 IMU_to_Vehicle_Offset_Z_0;
	uint8 IMU_to_Vehicle_Offset_Z_1;
	uint8 IMU_to_Vehicle_Offset_Z_2;
	uint8 INS_Timestamp_0;
	uint8 INS_Timestamp_1;
	uint8 INS_Timestamp_2;
	uint8 INS_Timestamp_3;
	uint8 INS_Timestamp_4;
	uint8 INS_Timestamp_5;
	uint8 INS_Timestamp_6;
	uint8 INS_Timestamp_7;
	uint8 INS_Timestamp_Valid;

	uint8 INS_146_TiDiffer_0;
	uint8 INS_146_TiDiffer_1;

	uint8 INS_IMU_X_Acc_0;
	uint8 INS_IMU_X_Acc_1;
	uint8 INS_IMU_X_Acc_2;
	uint8 INS_IMU_X_Rate_0;
	uint8 INS_IMU_X_Rate_1;
	uint8 INS_IMU_X_Rate_2;
	uint8 INS_IMU_Y_Acc_0;
	uint8 INS_IMU_Y_Acc_1;
	uint8 INS_IMU_Y_Acc_2;
	uint8 INS_IMU_Y_Rate_0;
	uint8 INS_IMU_Y_Rate_1;
	uint8 INS_IMU_Y_Rate_2;
	uint8 INS_IMU_Z_Acc_0;
	uint8 INS_IMU_Z_Acc_1;
	uint8 INS_IMU_Z_Acc_2;
	uint8 INS_IMU_Z_Rate_0;
	uint8 INS_IMU_Z_Rate_1;
	uint8 INS_IMU_Z_Rate_2;

	uint8 IMU_to_Vehicle_Error_Quaternion_W_0;
	uint8 IMU_to_Vehicle_Error_Quaternion_W_1;
	uint8 IMU_to_Vehicle_Error_Quaternion_W_2;
	uint8 IMU_to_Vehicle_Error_Quaternion_X_0;
	uint8 IMU_to_Vehicle_Error_Quaternion_X_1;
	uint8 IMU_to_Vehicle_Error_Quaternion_X_2;
	uint8 IMU_to_Vehicle_Error_Quaternion_Y_0;
	uint8 IMU_to_Vehicle_Error_Quaternion_Y_1;
	uint8 IMU_to_Vehicle_Error_Quaternion_Y_2;
	uint8 IMU_to_Vehicle_Error_Quaternion_Z_0;
	uint8 IMU_to_Vehicle_Error_Quaternion_Z_1;
	uint8 IMU_to_Vehicle_Error_Quaternion_Z_2;

	uint8 SlowDr_Status;
	uint8 INS_Vehicle_SlowDr_Pos_X_0;
	uint8 INS_Vehicle_SlowDr_Pos_X_1;
	uint8 INS_Vehicle_SlowDr_Pos_X_2;
	uint8 INS_Vehicle_SlowDr_Pos_X_3;
	uint8 INS_Vehicle_SlowDr_Pos_Y_0;
	uint8 INS_Vehicle_SlowDr_Pos_Y_1;
	uint8 INS_Vehicle_SlowDr_Pos_Y_2;
	uint8 INS_Vehicle_SlowDr_Pos_Y_3;
	uint8 INS_Vehicle_SlowDr_Pos_Z_0;
	uint8 INS_Vehicle_SlowDr_Pos_Z_1;
	uint8 INS_Vehicle_SlowDr_Pos_Z_2;
	uint8 INS_Vehicle_SlowDr_Pos_Z_3;
	uint8 INS_Vehicle_SlowDr_Roll_0;
	uint8 INS_Vehicle_SlowDr_Roll_1;
	uint8 INS_Vehicle_SlowDr_Roll_2;
	uint8 INS_Vehicle_SlowDr_Pitch_0;
	uint8 INS_Vehicle_SlowDr_Pitch_1;
	uint8 INS_Vehicle_SlowDr_Pitch_2;
	uint8 INS_Vehicle_SlowDr_Heading_0;
	uint8 INS_Vehicle_SlowDr_Heading_1;
	uint8 INS_Vehicle_SlowDr_Heading_2;
}_c_Enet_INS_Tx_146_msgType_t;


typedef union{
	uint8 _c[119];
	_c_Enet_INS_Tx_146_msgType_t	ins_146;
}_c_Enet_INS_Tx_146_buf_u;

typedef struct 
{
	uint8 INS_Current_Pos_Heading_0;
	uint8 INS_Current_Pos_Heading_1;
	uint8 INS_Current_Pos_Heading_2;
	uint8 INS_Current_Pos_Heading_Accuracy_0;
	uint8 INS_Current_Pos_Heading_Accuracy_1;
	uint8 INS_Current_Pos_Heading_Confidence;
	uint8 INS_Current_Pos_Height_Confidence;
	uint8 INS_Current_Pos_Lat_Confidence;
	uint8 INS_Vehicle_Lat_0;
	uint8 INS_Vehicle_Lat_1;
	uint8 INS_Vehicle_Lat_2;
	uint8 INS_Vehicle_Lat_3;
	uint8 INS_Current_Pos_Lat_GNSS_Err_0;
	uint8 INS_Current_Pos_Lat_GNSS_Err_1;
	uint8 INS_Current_Pos_Long_Confidence;
	uint8 INS_Vehicle_Lon_0;
	uint8 INS_Vehicle_Lon_1;
	uint8 INS_Vehicle_Lon_2;
	uint8 INS_Vehicle_Lon_3;
	uint8 INS_Current_Pos_Long_GNSS_Err_0;
	uint8 INS_Current_Pos_Long_GNSS_Err_1;
	uint8 INS_Current_Pos_Pitch_0;
	uint8 INS_Current_Pos_Pitch_1;
	uint8 INS_Current_Pos_Pitch_2;
	uint8 INS_Current_Pos_Pitch_Accuracy_0;
	uint8 INS_Current_Pos_Pitch_Accuracy_1;
	uint8 INS_Current_Pos_Pitch_Confidence;
	uint8 INS_Current_Pos_Roll_0;
	uint8 INS_Current_Pos_Roll_1;
	uint8 INS_Current_Pos_Roll_2;
	uint8 INS_Current_Pos_Roll_Accuracy_0;
	uint8 INS_Current_Pos_Roll_Accuracy_1;
	uint8 INS_Current_Pos_Roll_Confidence;//
	uint8 INS_GNSS_Height_0;
	uint8 INS_GNSS_Height_1;
	uint8 INS_GNSS_Height_2;
	uint8 INS_GNSS_Height_Err0_0;
	uint8 INS_GNSS_Height_Err0_1;
	uint8 INS_GNSS_Mode;	
	uint8 FL_wheel_vel_0;
	uint8 FL_wheel_vel_1;
	uint8 FR_wheel_vel_0;
	uint8 FR_wheel_vel_1;
	uint8 RL_wheel_vel_0;
	uint8 RL_wheel_vel_1;
	uint8 RR_wheel_vel_0;
	uint8 RR_wheel_vel_1;
	uint8 RL_wheel_factor_0;
	uint8 RL_wheel_factor_1;
	uint8 RR_wheel_factor_0;
	uint8 RR_wheel_factor_1;	
	uint8 INS_GPS_Week_0;
	uint8 INS_GPS_Week_1;
	uint8 INS_GPS_Time_0;
	uint8 INS_GPS_Time_1;
	uint8 INS_GPS_Time_2;
	uint8 INS_GPS_Time_3;
	uint8 INS_Timestamp_0;
	uint8 INS_Timestamp_1;
	uint8 INS_Timestamp_2;
	uint8 INS_Timestamp_3;
	uint8 INS_Timestamp_4;
	uint8 INS_Timestamp_5;
	uint8 INS_Timestamp_6;
	uint8 INS_Timestamp_7;
	uint8 INS_Timestamp_Valid;
	uint8 INS_POS_Match_RTK_POS_Mark;
	uint8 INS_17F_TiDiffer_0;
	uint8 INS_17F_TiDiffer_1;
}_c_Enet_INS_Tx_17F_msgType;

typedef union {
	uint8 _c[69];
	_c_Enet_INS_Tx_17F_msgType	ins_17F;
} _c_Enet_INS_Tx_17F_buf;

typedef struct 
{
	uint8 INS_GNSS_Time_Year_0;
	uint8 INS_GNSS_Time_Year_1;
	uint8 INS_GNSS_Time_Month;
	uint8 INS_GNSS_Time_Date;
	uint8 INS_GNSS_Time_Hour;
	uint8 INS_GNSS_Time_Minute;
	uint8 INS_GNSS_Time_Second;
	uint8 INS_GNSS_Time_mSecond_0;
	uint8 INS_GNSS_Time_mSecond_1;
	uint8 GNSS_Speed_0;
	uint8 GNSS_Speed_1;
	uint8 GNSS_Speed_2;
	uint8 GNSS_Speed_Err_0;
	uint8 GNSS_Speed_Err_1;
	uint8 INS_GNSS_Speed_North_0;
	uint8 INS_GNSS_Speed_North_1;
	uint8 INS_GNSS_Speed_North_2;
	uint8 INS_GNSS_Speed_East_0;
	uint8 INS_GNSS_Speed_East_1;
	uint8 INS_GNSS_Speed_East_2;
	uint8 INS_GNSS_Speed_Earth_0;
	uint8 INS_GNSS_Speed_Earth_1;
	uint8 INS_GNSS_Speed_Earth_2;
	uint8 INS_GNSS_Speed_North_Err_0;
	uint8 INS_GNSS_Speed_North_Err_1;
	uint8 INS_GNSS_Speed_East_Err_0;
	uint8 INS_GNSS_Speed_East_Err_1;
	uint8 INS_GNSS_Speed_Earth_Err_0;
	uint8 INS_GNSS_Speed_Earth_Err_1;
	uint8 INS_GNSS_Difference_delay_0;
	uint8 INS_GNSS_Difference_delay_1;
	uint8 INS_GNSS_Difference_delay_2;
	uint8 INS_GNSS_GDOP_0;
	uint8 INS_GNSS_GDOP_1;
	uint8 INS_GNSS_GDOP_2;
	uint8 INS_GNSS_PDOP_0;
	uint8 INS_GNSS_PDOP_1;
	uint8 INS_GNSS_PDOP_2;
	uint8 INS_GNSS_HDOP_0;
	uint8 INS_GNSS_HDOP_1;
	uint8 INS_GNSS_HDOP_2;
	uint8 INS_GNSS_VDOP_0;
	uint8 INS_GNSS_VDOP_1;
	uint8 INS_GNSS_VDOP_2;
	uint8 INS_GNSS_TDOP_0;
	uint8 INS_GNSS_TDOP_1;
	uint8 INS_GNSS_TDOP_2;
	uint8 INS_GNSS_Speed_East_Confidence;
	uint8 INS_GNSS_Speed_North_Confidence;
	uint8 INS_GNSS_Speed_Earth_Confidence;
	uint8 INS_WatchedSV;
	uint8 INS_UsedSV;
	uint8 INS_GPS_Flight_Path_Angle_0;
	uint8 INS_GPS_Flight_Path_Angle_1;
	uint8 INS_GPS_Flight_Path_Angle_2;
	uint8 INS_GNSS_Time_Valid;
}_c_Enet_INS_Tx_31B_msgType;

typedef union {
	uint8 _c[56];
	_c_Enet_INS_Tx_31B_msgType	ins_31B;
} _c_Enet_INS_Tx_31B_buf;

typedef struct 
{
	uint8 INS_GGA_TotByteLen_0;
	uint8 INS_GGA_TotByteLen_1;
	uint8 INS_GGA_Data[INS_GGA_DATA_NUMS];
}_c_Enet_INS_Tx_232_msgType;

typedef union {
	uint8 _c[INS_GGA_DATA_NUMS+INS_ETH_DATA_LENGH_BYTE];
	_c_Enet_INS_Tx_232_msgType	ins_232;
} _c_Enet_INS_Tx_232_buf;

typedef struct 
{
	uint8 INS_GSA_TotByteLen_0;
	uint8 INS_GSA_TotByteLen_1;
	uint8 INS_GSA_Data[INS_GSA_DATA_NUMS];
}_c_Enet_INS_Tx_233_msgType;

typedef union {
	uint8 _c[INS_GSA_DATA_NUMS+INS_ETH_DATA_LENGH_BYTE];
	_c_Enet_INS_Tx_233_msgType	ins_233;
} _c_Enet_INS_Tx_233_buf;

typedef struct 
{
	uint8 INS_GSV_TotByteLen_0;
	uint8 INS_GSV_TotByteLen_1;
	uint8 INS_GSV_Data[INS_GSV_DATA_NUMS];
}_c_Enet_INS_Tx_234_msgType;

typedef union {
	uint8 _c[INS_GSV_DATA_NUMS+INS_ETH_DATA_LENGH_BYTE];
	_c_Enet_INS_Tx_234_msgType	ins_234;
} _c_Enet_INS_Tx_234_buf;




typedef struct
{
    char desp[62];
    uint16 byteLenth;
    uint64 value;
    double factor;
    double offset;
    double result;
}msgDespInfo_t;

typedef union{
    struct{
        uint8  version;
        uint8 crc_len;
        uint16 pachet_count;
        uint32 length;
        uint32 message_type;
        uint32 crc_value;
        uint16 frag_set;
        uint16 frag_offset;
    }udpHead_t;
    uint8 head_buff[20];
}udpHead_u;

#pragma pack ()


#endif