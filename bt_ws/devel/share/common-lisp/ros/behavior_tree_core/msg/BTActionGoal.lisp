; Auto-generated. Do not edit!


(cl:in-package behavior_tree_core-msg)


;//! \htmlinclude BTActionGoal.msg.html

(cl:defclass <BTActionGoal> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (goal_id
    :reader goal_id
    :initarg :goal_id
    :type actionlib_msgs-msg:GoalID
    :initform (cl:make-instance 'actionlib_msgs-msg:GoalID))
   (goal
    :reader goal
    :initarg :goal
    :type behavior_tree_core-msg:BTGoal
    :initform (cl:make-instance 'behavior_tree_core-msg:BTGoal)))
)

(cl:defclass BTActionGoal (<BTActionGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BTActionGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BTActionGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name behavior_tree_core-msg:<BTActionGoal> is deprecated: use behavior_tree_core-msg:BTActionGoal instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <BTActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader behavior_tree_core-msg:header-val is deprecated.  Use behavior_tree_core-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'goal_id-val :lambda-list '(m))
(cl:defmethod goal_id-val ((m <BTActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader behavior_tree_core-msg:goal_id-val is deprecated.  Use behavior_tree_core-msg:goal_id instead.")
  (goal_id m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <BTActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader behavior_tree_core-msg:goal-val is deprecated.  Use behavior_tree_core-msg:goal instead.")
  (goal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BTActionGoal>) ostream)
  "Serializes a message object of type '<BTActionGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal_id) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BTActionGoal>) istream)
  "Deserializes a message object of type '<BTActionGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal_id) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BTActionGoal>)))
  "Returns string type for a message object of type '<BTActionGoal>"
  "behavior_tree_core/BTActionGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BTActionGoal)))
  "Returns string type for a message object of type 'BTActionGoal"
  "behavior_tree_core/BTActionGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BTActionGoal>)))
  "Returns md5sum for a message object of type '<BTActionGoal>"
  "5fd1195e2b220412a879115d80874d64")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BTActionGoal)))
  "Returns md5sum for a message object of type 'BTActionGoal"
  "5fd1195e2b220412a879115d80874d64")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BTActionGoal>)))
  "Returns full string definition for message of type '<BTActionGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%BTGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: behavior_tree_core/BTGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal definition~%int32 parameter #no goal needed for BT tick. But It could be useful to have a parameter for action (e.g.goto x,y)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BTActionGoal)))
  "Returns full string definition for message of type 'BTActionGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%BTGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: behavior_tree_core/BTGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal definition~%int32 parameter #no goal needed for BT tick. But It could be useful to have a parameter for action (e.g.goto x,y)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BTActionGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal_id))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BTActionGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'BTActionGoal
    (cl:cons ':header (header msg))
    (cl:cons ':goal_id (goal_id msg))
    (cl:cons ':goal (goal msg))
))
