SELECT A.LotID,A.DeviceID,A.ProcessID , C.OperationID, C.ParameterId, C.MeasuredValue as MV, C.WaferNo, E.UpperHoldValue as USL, E.LowerHoldValue as LSL, E.UpperControlLimit as UCL, E.LowerControlLimit as LCL
FROM
    LLotStart A
    inner join LOperationMeasuredValueRaw C on C.LotID = A.LotID
    inner join ParameterIdForRnQA1 B on B.ParameterId  = C.ParameterId
    inner join LOperationLimits E on E.OpParameterID = B.ParameterId and E.OperationID = C.OperationID
    inner join LOperationParameterUnit F on F.OpParameterId = B.ParameterId and F.OperationID = C.OperationID
WHERE A.LotID like 'F%' and ProcessID = 'Product Flow 1.8V/3.3V w'	
order by C.ParameterId, LotID desc