
function out=slice(dat,N,n,dir)
  n=floor(n); ## Be sure to take integer part to avoid errors
  if n<1
    printf("\nAsking for non-existent slice, n=#f.\n\n",n)
    return
  endif
  
  if dir==3
    if n>N(3)
      printf("\nAsking for non-existent slice, n=#f.\n\n",n)
      return
    endif
    dat=reshape(dat,N(1)*N(2),N(3)); ## Group into matrix with dir=3 as cols
    out=reshape(dat[:,n),N(1),N(2)]; ## Take n-th col and reshape as slice
  elseif dir==2 
    if n>N(2)
      printf("\nAsking for non-existent slice, n=#f.\n\n",n)
      return
    endif
    dat=reshape(dat,N(1)*N(2),N(3)); ## Group to expose N(2)
    dat=conj(dat'); ## dat is now in order N(3),N(1)*N(2)
    dat=reshape(dat,N(3)*N(1),N(2)); ## Form with dir=2 as cols
    out=reshape(dat[:,n),N(3),N(1)]; ## Shape into slice
    out=conj(out'); ## Reorder as N(1),N(3)
  elseif dir==1
    if n>N(1)
      printf("\nAsking for non-existent slice, n=#f.\n\n",n)
      return
    endif
    dat=reshape(dat,N(1),N(2)*N(3)); ## Group to expose N(1)
    dat=conj(dat'); ## dat is now N(2)*N(3),N(1)
    out=reshape(dat[:,n),N(2),N(3)]
  else
    printf("\nError in slice(): invalid choice for dir.  dir=#f\n\n",dir)
  endif

endfunction
