(include "book-queue.scm")
(include "wire.scm")
(include "and-gate.scm")
(include "or-gate.scm")
(include "inverter.scm")
(include "adders.scm")

(define (probe name wire)
    (add-action! wire
                (lambda ()
                    (newline)
                    (display (current-time the-agenda))
                    (display " | ")
                    (display name)
                    (display " changed to: ")
                    (display (get-signal wire))
                    (newline)
                )
    )
)

(define the-agenda (make-agenda))
(define inverter-delay 2)
(define and-gate-delay 3)
(define or-gate-delay 5)

(define input-1 (make-wire))
(define input-2 (make-wire))
(define sum (make-wire))
(define carry (make-wire))

(probe 'sum sum)
(probe 'carry carry)

(half-adder input-1 input-2 sum carry)

(set-signal! input-1 1)

(propagate)

(set-signal! input-2 1)

(propagate)