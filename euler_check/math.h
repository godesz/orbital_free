#ifndef LEMON_MATH_H
#define LEMON_MATH_H

///\ingroup misc
///\file
///\brief Some extensions to the standard \c cmath library.
///
///Some extensions to the standard \c cmath library.
///
///This file includes the standard math library (cmath).

#include<cmath>

namespace lemon {

  /// \addtogroup misc
  /// @{

  /// The Euler constant
  const long double E       = 2.7182818284590452353602874713526625L;
  /// log_2(e)
  const long double LOG2E   = 1.4426950408889634073599246810018921L;
  /// log_10(e)
  const long double LOG10E  = 0.4342944819032518276511289189166051L;
  /// ln(2)
  const long double LN2     = 0.6931471805599453094172321214581766L;
  /// ln(10)
  const long double LN10    = 2.3025850929940456840179914546843642L;
  /// pi
  const long double PI      = 3.1415926535897932384626433832795029L;
  /// pi/2
  const long double PI_2    = 1.5707963267948966192313216916397514L;
  /// pi/4
  const long double PI_4    = 0.7853981633974483096156608458198757L;
  /// sqrt(2)
  const long double SQRT2   = 1.4142135623730950488016887242096981L;
  /// 1/sqrt(2)
  const long double SQRT1_2 = 0.7071067811865475244008443621048490L;

  ///Check whether the parameter is NaN or not

  ///This function checks whether the parameter is NaN or not.
  ///Is should be equivalent with std::isnan(), but it is not
  ///provided by all compilers.
  inline bool isNaN(double v)
    {
      return v!=v;
    }

  /// @}

} //namespace lemon

#endif //LEMON_TOLERANCE_H
