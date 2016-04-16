; priority queue
(define (pq)
  (define events nil)
  (define clock 0)
  ; skip is how much time before the function occurs
  ; f is the function to run at that time
  (define (insert skip f)
    ; an absolute time which represents when the actual
    ;  function gets ran
    (define when (+ clock skip))
    (define (iter items)
      (cond
        ((null? items)
          ; return one tuple with when and function
          (list (list when f))
        )
        ((< when (car (car items)))
          (cons (list when f) items)
        )
        (else
          (cons (car items) (iter (cdr items)))
        ))
    )
    (set! events (iter events))
  )
  ; book calls go propagate
  (define (go)
    (cond
      ((null? events)
        'DONE
      )
      (else
        (define event (car events))
        (set! events (cdr events))
        (set! clock (car event))
        ((cadr event))
        (go)
      ))
  )
  (define (peekTime)
    (if (null? events)
      clock
      (car (car events))
    )
  )
  (define (peekFunction) (cadr (car events)))
  ; you should also make a print function
  this
)

; (define q (pq))
; ((q'insert) 16
;     (lambda ()
;         (print ((q'peekTime)) " | ")
;         (println "Hello, World!")
;         ((g'insert) 9
;             (lambda ()
;                 (print ((q'peekTime)) " | ")
;                 (println "good-bye\n")
;                 )
;             )
;         )
;     )
; ((q'go))
