; list of holders = nil
; p use gettid to add to list of holders
; v check gettid to see if there

(define m (mmutex 3))
((m'p))
; ACQUIRED
gettid
