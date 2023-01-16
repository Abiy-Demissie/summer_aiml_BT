# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from greenball_tracking/HighCmd.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import greenball_tracking.msg

class HighCmd(genpy.Message):
  _md5sum = "b4825051cf66ae8183b54c57dba16b66"
  _type = "greenball_tracking/HighCmd"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8[2] head
uint8 levelFlag
uint8 frameReserve

uint32[2] SN
uint32[2] version
uint16 bandWidth
uint8 mode 

uint8 gaitType		   
uint8 speedLevel			   
float32 footRaiseHeight		   
float32 bodyHeight	   
float32[2] position 
float32[3] euler	   
float32[2] velocity 
float32 yawSpeed				   
BmsCmd bms
LED[4] led
uint8[40] wirelessRemote
uint32 reserve

uint32 crc
================================================================================
MSG: greenball_tracking/BmsCmd
uint8 off            # off 0xA5
uint8[3] reserve
================================================================================
MSG: greenball_tracking/LED
uint8 r
uint8 g
uint8 b"""
  __slots__ = ['head','levelFlag','frameReserve','SN','version','bandWidth','mode','gaitType','speedLevel','footRaiseHeight','bodyHeight','position','euler','velocity','yawSpeed','bms','led','wirelessRemote','reserve','crc']
  _slot_types = ['uint8[2]','uint8','uint8','uint32[2]','uint32[2]','uint16','uint8','uint8','uint8','float32','float32','float32[2]','float32[3]','float32[2]','float32','greenball_tracking/BmsCmd','greenball_tracking/LED[4]','uint8[40]','uint32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       head,levelFlag,frameReserve,SN,version,bandWidth,mode,gaitType,speedLevel,footRaiseHeight,bodyHeight,position,euler,velocity,yawSpeed,bms,led,wirelessRemote,reserve,crc

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HighCmd, self).__init__(*args, **kwds)
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
      if self.mode is None:
        self.mode = 0
      if self.gaitType is None:
        self.gaitType = 0
      if self.speedLevel is None:
        self.speedLevel = 0
      if self.footRaiseHeight is None:
        self.footRaiseHeight = 0.
      if self.bodyHeight is None:
        self.bodyHeight = 0.
      if self.position is None:
        self.position = [0.] * 2
      if self.euler is None:
        self.euler = [0.] * 3
      if self.velocity is None:
        self.velocity = [0.] * 2
      if self.yawSpeed is None:
        self.yawSpeed = 0.
      if self.bms is None:
        self.bms = greenball_tracking.msg.BmsCmd()
      if self.led is None:
        self.led = [greenball_tracking.msg.LED() for _ in range(4)]
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
      self.mode = 0
      self.gaitType = 0
      self.speedLevel = 0
      self.footRaiseHeight = 0.
      self.bodyHeight = 0.
      self.position = [0.] * 2
      self.euler = [0.] * 3
      self.velocity = [0.] * 2
      self.yawSpeed = 0.
      self.bms = greenball_tracking.msg.BmsCmd()
      self.led = [greenball_tracking.msg.LED() for _ in range(4)]
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
      _x = self
      buff.write(_get_struct_H3B2f().pack(_x.bandWidth, _x.mode, _x.gaitType, _x.speedLevel, _x.footRaiseHeight, _x.bodyHeight))
      buff.write(_get_struct_2f().pack(*self.position))
      buff.write(_get_struct_3f().pack(*self.euler))
      buff.write(_get_struct_2f().pack(*self.velocity))
      _x = self
      buff.write(_get_struct_fB().pack(_x.yawSpeed, _x.bms.off))
      _x = self.bms.reserve
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_3B().pack(*_x))
      else:
        buff.write(_get_struct_3s().pack(_x))
      if len(self.led) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.led), 'self.led')))
      for val1 in self.led:
        _x = val1
        buff.write(_get_struct_3B().pack(_x.r, _x.g, _x.b))
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
      if self.bms is None:
        self.bms = greenball_tracking.msg.BmsCmd()
      if self.led is None:
        self.led = None
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
      _x = self
      start = end
      end += 13
      (_x.bandWidth, _x.mode, _x.gaitType, _x.speedLevel, _x.footRaiseHeight, _x.bodyHeight,) = _get_struct_H3B2f().unpack(str[start:end])
      start = end
      end += 8
      self.position = _get_struct_2f().unpack(str[start:end])
      start = end
      end += 12
      self.euler = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 8
      self.velocity = _get_struct_2f().unpack(str[start:end])
      _x = self
      start = end
      end += 5
      (_x.yawSpeed, _x.bms.off,) = _get_struct_fB().unpack(str[start:end])
      start = end
      end += 3
      self.bms.reserve = str[start:end]
      self.led = []
      for i in range(0, 4):
        val1 = greenball_tracking.msg.LED()
        _x = val1
        start = end
        end += 3
        (_x.r, _x.g, _x.b,) = _get_struct_3B().unpack(str[start:end])
        self.led.append(val1)
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
      _x = self
      buff.write(_get_struct_H3B2f().pack(_x.bandWidth, _x.mode, _x.gaitType, _x.speedLevel, _x.footRaiseHeight, _x.bodyHeight))
      buff.write(self.position.tostring())
      buff.write(self.euler.tostring())
      buff.write(self.velocity.tostring())
      _x = self
      buff.write(_get_struct_fB().pack(_x.yawSpeed, _x.bms.off))
      _x = self.bms.reserve
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_3B().pack(*_x))
      else:
        buff.write(_get_struct_3s().pack(_x))
      if len(self.led) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.led), 'self.led')))
      for val1 in self.led:
        _x = val1
        buff.write(_get_struct_3B().pack(_x.r, _x.g, _x.b))
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
      if self.bms is None:
        self.bms = greenball_tracking.msg.BmsCmd()
      if self.led is None:
        self.led = None
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
      _x = self
      start = end
      end += 13
      (_x.bandWidth, _x.mode, _x.gaitType, _x.speedLevel, _x.footRaiseHeight, _x.bodyHeight,) = _get_struct_H3B2f().unpack(str[start:end])
      start = end
      end += 8
      self.position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
      start = end
      end += 12
      self.euler = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 8
      self.velocity = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
      _x = self
      start = end
      end += 5
      (_x.yawSpeed, _x.bms.off,) = _get_struct_fB().unpack(str[start:end])
      start = end
      end += 3
      self.bms.reserve = str[start:end]
      self.led = []
      for i in range(0, 4):
        val1 = greenball_tracking.msg.LED()
        _x = val1
        start = end
        end += 3
        (_x.r, _x.g, _x.b,) = _get_struct_3B().unpack(str[start:end])
        self.led.append(val1)
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
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_2s = None
def _get_struct_2s():
    global _struct_2s
    if _struct_2s is None:
        _struct_2s = struct.Struct("<2s")
    return _struct_2s
_struct_3B = None
def _get_struct_3B():
    global _struct_3B
    if _struct_3B is None:
        _struct_3B = struct.Struct("<3B")
    return _struct_3B
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_3s = None
def _get_struct_3s():
    global _struct_3s
    if _struct_3s is None:
        _struct_3s = struct.Struct("<3s")
    return _struct_3s
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
_struct_H3B2f = None
def _get_struct_H3B2f():
    global _struct_H3B2f
    if _struct_H3B2f is None:
        _struct_H3B2f = struct.Struct("<H3B2f")
    return _struct_H3B2f
_struct_fB = None
def _get_struct_fB():
    global _struct_fB
    if _struct_fB is None:
        _struct_fB = struct.Struct("<fB")
    return _struct_fB
