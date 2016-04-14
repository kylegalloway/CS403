(define (run-all items)
  (cond
	((null? items) nil)
	(else
	  ((car items))
	  (run-all (cdr items))
	  )
	)
  )

(define (wire)
  (define signal 0)

  (define endpoints nil)

  (define (get)
	signal
	)

  (define (set v)
	(cond
	  ((!= v signal)
	   (set! signal v)
	   (run-all endpoints)
	   )
	  )
	)

  (define (add f)
	(set! endpoints (cons f endpoints))
	(f)
	)

  this
  )

(define (and-gate q in1 in2 out)
  (define delay 4)

  (define (action)
	(define inv1 ((get 'get in1)))
	(define inv2 ((get 'get in2)))
	((get 'delay q) delay
					(lambda ()
					  (if (and (>= inv1 0.5) (>= inv2 0.5))
						((get 'set out) 1)
						((get 'set out) 0)
						)
					  )
					)
	)

  ((get 'add in1) action)
  ((get 'add in2) action)

  nil
  )

(define (probe q w name)
  (define (action)
	(define delay 1)
	((get 'insert q) delay
					 (lambda ()
					   (println ((get 'peekTime q)) ": wire " name " has a new value: " ((get 'get w)))
					   )
					 )
	)

  ((get 'add w) action)
  )

(define (pq)
  this
  )

(define (main)
  (define q (pq))

  (define a (wire))
  (define b (wire))
  (define c (wire))

  (probe q a 'a)
  (probe q b 'b)
  (probe q c 'c)

  (and-gate q a b c)

  ((get 'set a) 1)
  ((get 'set b) 1)
  )

(main)
