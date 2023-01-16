# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from greenball_tracking/HighState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import greenball_tracking.msg

class HighState(genpy.Message):
  _md5sum = "7904f43019dadf7640d573b4c14b9066"
  _type = "greenball_tracking/HighState"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
uint8[2] head
uint8 levelFlag
uint8 frameReserve

uint32[2] SN
uint32[2] version
uint16 bandWidth
IMU imu
MotorState[20] motorState
BmsState bms
int16[4] footForce
int16[4] footForceEst
uint8 mode
float32 progress
uint8 gaitType		   
float32 footRaiseHeight		  
float32[3] position 
float32 bodyHeight			  
float32[3] velocity 
float32 yawSpeed				   
float32[4] rangeObstacle
Cartesian[4] footPosition2Body 
Cartesian[4] footSpeed2Body	
uint8[40] wirelessRemote
uint32 reserve

uint32 crc
================================================================================
MSG: greenball_tracking/IMU
float32[4] quaternion
float32[3] gyroscope
float32[3] accelerometer
float32[3] rpy
int8 temperature
================================================================================
MSG: greenball_tracking/MotorState
uint8 mode           # motor current mode 
float32 q            # motor current position（rad）
float32 dq           # motor current speed（rad/s）
float32 ddq          # motor current speed（rad/s）
float32 tauEst       # current estimated output torque（N*m）
float32 q_raw        # motor current position（rad）
float32 dq_raw       # motor current speed（rad/s）
float32 ddq_raw      # motor current speed（rad/s）
int8 temperature     # motor temperature（slow conduction of temperature leads to lag）
uint32[2] reserve
================================================================================
MSG: greenball_tracking/BmsState
uint8 version_h
uint8 version_l
uint8 bms_status
uint8 SOC                  # SOC 0-100%
int32 current              # mA
uint16 cycle
int8[2] BQ_NTC             # x1 degrees centigrade
int8[2] MCU_NTC            # x1 degrees centigrade
uint16[10] cell_vol        # cell voltage mV
================================================================================
MSG: greenball_tracking/Cartesian
float32 x
float32 y
float32 z"""
  __slots__ = ['head','levelFlag','frameReserve','SN','version','bandWidth','imu','motorState','bms','footForce','footForceEst','mode','progress','gaitType','footRaiseHeight','position','bodyHeight','velocity','yawSpeed','rangeObstacle','footPosition2Body','footSpeed2Body','wirelessRemote','reserve','crc']
  _slot_types = ['uint8[2]','uint8','uint8','uint32[2]','uint32[2]','uint16','greenball_tracking/IMU','greenball_tracking/MotorState[20]','greenball_tracking/BmsState','int16[4]','int16[4]','uint8','float32','uint8','float32','float32[3]','float32','float32[3]','float32','float32[4]','greenball_tracking/Cartesian[4]','greenball_tracking/Cartesian[4]','uint8[40]','uint32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       head,levelFlag,frameReserve,SN,version,bandWidth,imu,motorState,bms,footForce,footForceEst,mode,progress,gaitType,footRaiseHeight,position,bodyHeight,velocity,yawSpeed,rangeObstacle,footPosition2Body,footSpeed2Body,wirelessRemote,reserve,crc

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HighState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.head is None:
        self.head = b'\0'*2
      if self.levelFlag is None:
        self.levelFlag = 0
      if self.frameReserve is None:
        self.frameReserve = 0
      if self.SN is None:
        self.SN = [0] * 2
      if self.version is None:
        self.version = [0] * 2
      if self.bandWidth is None:
        self.bandWidth = 0
      if self.imu is None:
        self.imu = greenball_tracking.msg.IMU()
      if self.motorState is None:
        self.motorState = [greenball_tracking.msg.MotorState() for _ in range(20)]
      if self.bms is None:
        self.bms = greenball_tracking.msg.BmsState()
      if self.footForce is None:
        self.footForce = [0] * 4
      if self.footForceEst is None:
        self.footForceEst = [0] * 4
      if self.mode is None:
        self.mode = 0
      if self.progress is None:
        self.progress = 0.
      if self.gaitType is None:
        self.gaitType = 0
      if self.footRaiseHeight is None:
        self.footRaiseHeight = 0.
      if self.position is None:
        self.position = [0.] * 3
      if self.bodyHeight is None:
        self.bodyHeight = 0.
      if self.velocity is None:
        self.velocity = [0.] * 3
      if self.yawSpeed is None:
        self.yawSpeed = 0.
      if self.rangeObstacle is None:
        self.rangeObstacle = [0.] * 4
      if self.footPosition2Body is None:
        self.footPosition2Body = [greenball_tracking.msg.Cartesian() for _ in range(4)]
      if self.footSpeed2Body is None:
        self.footSpeed2Body = [greenball_tracking.msg.Cartesian() for _ in range(4)]
      if self.wirelessRemote is None:
        self.wirelessRemote = b'\0'*40
      if self.reserve is None:
        self.reserve = 0
      if self.crc is None:
        self.crc = 0
    else:
      self.head = b'\0'*2
      self.levelFlag = 0
      self.frameReserve = 0
      self.SN = [0] * 2
      self.version = [0] * 2
      self.bandWidth = 0
      self.imu = greenball_tracking.msg.IMU()
      self.motorState = [greenball_tracking.msg.MotorState() for _ in range(20)]
      self.bms = greenball_tracking.msg.BmsState()
      self.footForce = [0] * 4
      self.footForceEst = [0] * 4
      self.mode = 0
      self.progress = 0.
      self.gaitType = 0
      self.footRaiseHeight = 0.
      self.position = [0.] * 3
      self.bodyHeight = 0.
      self.velocity = [0.] * 3
      self.yawSpeed = 0.
      self.rangeObstacle = [0.] * 4
      self.footPosition2Body = [greenball_tracking.msg.Cartesian() for _ in range(4)]
      self.footSpeed2Body = [greenball_tracking.msg.Cartesian() for _ in range(4)]
      self.wirelessRemote = b'\0'*40
      self.reserve = 0
      self.crc = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.head
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_2B().pack(*_x))
      else:
        buff.write(_get_struct_2s().pack(_x))
      _x = self
      buff.write(_get_struct_2B().pack(_x.levelFlag, _x.frameReserve))
      buff.write(_get_struct_2I().pack(*self.SN))
      buff.write(_get_struct_2I().pack(*self.version))
      _x = self.bandWidth
      buff.write(_get_struct_H().pack(_x))
      buff.write(_get_struct_4f().pack(*self.imu.quaternion))
      buff.write(_get_struct_3f().pack(*self.imu.gyroscope))
      buff.write(_get_struct_3f().pack(*self.imu.accelerometer))
      buff.write(_get_struct_3f().pack(*self.imu.rpy))
      _x = self.imu.temperature
      buff.write(_get_struct_b().pack(_x))
      if len(self.motorState) != 20:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (20, len(self.motorState), 'self.motorState')))
      for val1 in self.motorState:
        _x = val1
        buff.write(_get_struct_B7fb().pack(_x.mode, _x.q, _x.dq, _x.ddq, _x.tauEst, _x.q_raw, _x.dq_raw, _x.ddq_raw, _x.temperature))
        buff.write(_get_struct_2I().pack(*val1.reserve))
      _x = self
      buff.write(_get_struct_4BiH().pack(_x.bms.version_h, _x.bms.version_l, _x.bms.bms_status, _x.bms.SOC, _x.bms.current, _x.bms.cycle))
      buff.write(_get_struct_2b().pack(*self.bms.BQ_NTC))
      buff.write(_get_struct_2b().pack(*self.bms.MCU_NTC))
      buff.write(_get_struct_10H().pack(*self.bms.cell_vol))
      buff.write(_get_struct_4h().pack(*self.footForce))
      buff.write(_get_struct_4h().pack(*self.footForceEst))
      _x = self
      buff.write(_get_struct_BfBf().pack(_x.mode, _x.progress, _x.gaitType, _x.footRaiseHeight))
      buff.write(_get_struct_3f().pack(*self.position))
      _x = self.bodyHeight
      buff.write(_get_struct_f().pack(_x))
      buff.write(_get_struct_3f().pack(*self.velocity))
      _x = self.yawSpeed
      buff.write(_get_struct_f().pack(_x))
      buff.write(_get_struct_4f().pack(*self.rangeObstacle))
      if len(self.footPosition2Body) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.footPosition2Body), 'self.footPosition2Body')))
      for val1 in self.footPosition2Body:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      if len(self.footSpeed2Body) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.footSpeed2Body), 'self.footSpeed2Body')))
      for val1 in self.footSpeed2Body:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      _x = self.wirelessRemote
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_40B().pack(*_x))
      else:
        buff.write(_get_struct_40s().pack(_x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.reserve, _x.crc))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.imu is None:
        self.imu = greenball_tracking.msg.IMU()
      if self.motorState is None:
        self.motorState = None
      if self.bms is None:
        self.bms = greenball_tracking.msg.BmsState()
      if self.footPosition2Body is None:
        self.footPosition2Body = None
      if self.footSpeed2Body is None:
        self.footSpeed2Body = None
      end = 0
      start = end
      end += 2
      self.head = str[start:end]
      _x = self
      start = end
      end += 2
      (_x.levelFlag, _x.frameReserve,) = _get_struct_2B().unpack(str[start:end])
      start = end
      end += 8
      self.SN = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 8
      self.version = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 2
      (self.bandWidth,) = _get_struct_H().unpack(str[start:end])
      start = end
      end += 16
      self.imu.quaternion = _get_struct_4f().unpack(str[start:end])
      start = end
      end += 12
      self.imu.gyroscope = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.imu.accelerometer = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.imu.rpy = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 1
      (self.imu.temperature,) = _get_struct_b().unpack(str[start:end])
      self.motorState = []
      for i in range(0, 20):
        val1 = greenball_tracking.msg.MotorState()
        _x = val1
        start = end
        end += 30
        (_x.mode, _x.q, _x.dq, _x.ddq, _x.tauEst, _x.q_raw, _x.dq_raw, _x.ddq_raw, _x.temperature,) = _get_struct_B7fb().unpack(str[start:end])
        start = end
        end += 8
        val1.reserve = _get_struct_2I().unpack(str[start:end])
        self.motorState.append(val1)
      _x = self
      start = end
      end += 10
      (_x.bms.version_h, _x.bms.version_l, _x.bms.bms_status, _x.bms.SOC, _x.bms.current, _x.bms.cycle,) = _get_struct_4BiH().unpack(str[start:end])
      start = end
      end += 2
      self.bms.BQ_NTC = _get_struct_2b().unpack(str[start:end])
      start = end
      end += 2
      self.bms.MCU_NTC = _get_struct_2b().unpack(str[start:end])
      start = end
      end += 20
      self.bms.cell_vol = _get_struct_10H().unpack(str[start:end])
      start = end
      end += 8
      self.footForce = _get_struct_4h().unpack(str[start:end])
      start = end
      end += 8
      self.footForceEst = _get_struct_4h().unpack(str[start:end])
      _x = self
      start = end
      end += 10
      (_x.mode, _x.progress, _x.gaitType, _x.footRaiseHeight,) = _get_struct_BfBf().unpack(str[start:end])
      start = end
      end += 12
      self.position = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 4
      (self.bodyHeight,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 12
      self.velocity = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 4
      (self.yawSpeed,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 16
      self.rangeObstacle = _get_struct_4f().unpack(str[start:end])
      self.footPosition2Body = []
      for i in range(0, 4):
        val1 = greenball_tracking.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.footPosition2Body.append(val1)
      self.footSpeed2Body = []
      for i in range(0, 4):
        val1 = greenball_tracking.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.footSpeed2Body.append(val1)
      start = end
      end += 40
      self.wirelessRemote = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.reserve, _x.crc,) = _get_struct_2I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.head
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_2B().pack(*_x))
      else:
        buff.write(_get_struct_2s().pack(_x))
      _x = self
      buff.write(_get_struct_2B().pack(_x.levelFlag, _x.frameReserve))
      buff.write(self.SN.tostring())
      buff.write(self.version.tostring())
      _x = self.bandWidth
      buff.write(_get_struct_H().pack(_x))
      buff.write(self.imu.quaternion.tostring())
      buff.write(self.imu.gyroscope.tostring())
      buff.write(self.imu.accelerometer.tostring())
      buff.write(self.imu.rpy.tostring())
      _x = self.imu.temperature
      buff.write(_get_struct_b().pack(_x))
      if len(self.motorState) != 20:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (20, len(self.motorState), 'self.motorState')))
      for val1 in self.motorState:
        _x = val1
        buff.write(_get_struct_B7fb().pack(_x.mode, _x.q, _x.dq, _x.ddq, _x.tauEst, _x.q_raw, _x.dq_raw, _x.ddq_raw, _x.temperature))
        buff.write(val1.reserve.tostring())
      _x = self
      buff.write(_get_struct_4BiH().pack(_x.bms.version_h, _x.bms.version_l, _x.bms.bms_status, _x.bms.SOC, _x.bms.current, _x.bms.cycle))
      buff.write(self.bms.BQ_NTC.tostring())
      buff.write(self.bms.MCU_NTC.tostring())
      buff.write(self.bms.cell_vol.tostring())
      buff.write(self.footForce.tostring())
      buff.write(self.footForceEst.tostring())
      _x = self
      buff.write(_get_struct_BfBf().pack(_x.mode, _x.progress, _x.gaitType, _x.footRaiseHeight))
      buff.write(self.position.tostring())
      _x = self.bodyHeight
      buff.write(_get_struct_f().pack(_x))
      buff.write(self.velocity.tostring())
      _x = self.yawSpeed
      buff.write(_get_struct_f().pack(_x))
      buff.write(self.rangeObstacle.tostring())
      if len(self.footPosition2Body) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.footPosition2Body), 'self.footPosition2Body')))
      for val1 in self.footPosition2Body:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      if len(self.footSpeed2Body) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.footSpeed2Body), 'self.footSpeed2Body')))
      for val1 in self.footSpeed2Body:
        _x = val1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
      _x = self.wirelessRemote
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_40B().pack(*_x))
      else:
        buff.write(_get_struct_40s().pack(_x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.reserve, _x.crc))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.imu is None:
        self.imu = greenball_tracking.msg.IMU()
      if self.motorState is None:
        self.motorState = None
      if self.bms is None:
        self.bms = greenball_tracking.msg.BmsState()
      if self.footPosition2Body is None:
        self.footPosition2Body = None
      if self.footSpeed2Body is None:
        self.footSpeed2Body = None
      end = 0
      start = end
      end += 2
      self.head = str[start:end]
      _x = self
      start = end
      end += 2
      (_x.levelFlag, _x.frameReserve,) = _get_struct_2B().unpack(str[start:end])
      start = end
      end += 8
      self.SN = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=2)
      start = end
      end += 8
      self.version = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=2)
      start = end
      end += 2
      (self.bandWidth,) = _get_struct_H().unpack(str[start:end])
      start = end
      end += 16
      self.imu.quaternion = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=4)
      start = end
      end += 12
      self.imu.gyroscope = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.imu.accelerometer = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.imu.rpy = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 1
      (self.imu.temperature,) = _get_struct_b().unpack(str[start:end])
      self.motorState = []
      for i in range(0, 20):
        val1 = greenball_tracking.msg.MotorState()
        _x = val1
        start = end
        end += 30
        (_x.mode, _x.q, _x.dq, _x.ddq, _x.tauEst, _x.q_raw, _x.dq_raw, _x.ddq_raw, _x.temperature,) = _get_struct_B7fb().unpack(str[start:end])
        start = end
        end += 8
        val1.reserve = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=2)
        self.motorState.append(val1)
      _x = self
      start = end
      end += 10
      (_x.bms.version_h, _x.bms.version_l, _x.bms.bms_status, _x.bms.SOC, _x.bms.current, _x.bms.cycle,) = _get_struct_4BiH().unpack(str[start:end])
      start = end
      end += 2
      self.bms.BQ_NTC = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=2)
      start = end
      end += 2
      self.bms.MCU_NTC = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=2)
      start = end
      end += 20
      self.bms.cell_vol = numpy.frombuffer(str[start:end], dtype=numpy.uint16, count=10)
      start = end
      end += 8
      self.footForce = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=4)
      start = end
      end += 8
      self.footForceEst = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=4)
      _x = self
      start = end
      end += 10
      (_x.mode, _x.progress, _x.gaitType, _x.footRaiseHeight,) = _get_struct_BfBf().unpack(str[start:end])
      start = end
      end += 12
      self.position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 4
      (self.bodyHeight,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 12
      self.velocity = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 4
      (self.yawSpeed,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 16
      self.rangeObstacle = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=4)
      self.footPosition2Body = []
      for i in range(0, 4):
        val1 = greenball_tracking.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.footPosition2Body.append(val1)
      self.footSpeed2Body = []
      for i in range(0, 4):
        val1 = greenball_tracking.msg.Cartesian()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        self.footSpeed2Body.append(val1)
      start = end
      end += 40
      self.wirelessRemote = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.reserve, _x.crc,) = _get_struct_2I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_10H = None
def _get_struct_10H():
    global _struct_10H
    if _struct_10H is None:
        _struct_10H = struct.Struct("<10H")
    return _struct_10H
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_2b = None
def _get_struct_2b():
    global _struct_2b
    if _struct_2b is None:
        _struct_2b = struct.Struct("<2b")
    return _struct_2b
_struct_2s = None
def _get_struct_2s():
    global _struct_2s
    if _struct_2s is None:
        _struct_2s = struct.Struct("<2s")
    return _struct_2s
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_40B = None
def _get_struct_40B():
    global _struct_40B
    if _struct_40B is None:
        _struct_40B = struct.Struct("<40B")
    return _struct_40B
_struct_40s = None
def _get_struct_40s():
    global _struct_40s
    if _struct_40s is None:
        _struct_40s = struct.Struct("<40s")
    return _struct_40s
_struct_4BiH = None
def _get_struct_4BiH():
    global _struct_4BiH
    if _struct_4BiH is None:
        _struct_4BiH = struct.Struct("<4BiH")
    return _struct_4BiH
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
_struct_4h = None
def _get_struct_4h():
    global _struct_4h
    if _struct_4h is None:
        _struct_4h = struct.Struct("<4h")
    return _struct_4h
_struct_B7fb = None
def _get_struct_B7fb():
    global _struct_B7fb
    if _struct_B7fb is None:
        _struct_B7fb = struct.Struct("<B7fb")
    return _struct_B7fb
_struct_BfBf = None
def _get_struct_BfBf():
    global _struct_BfBf
    if _struct_BfBf is None:
        _struct_BfBf = struct.Struct("<BfBf")
    return _struct_BfBf
_struct_H = None
def _get_struct_H():
    global _struct_H
    if _struct_H is None:
        _struct_H = struct.Struct("<H")
    return _struct_H
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
