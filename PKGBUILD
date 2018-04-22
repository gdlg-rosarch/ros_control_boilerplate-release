# Script generated with Bloom
pkgdesc="ROS - Simple simulation interface and template for setting up a hardware interface for ros_control"
url='https://github.com/davetcoleman/ros_control_boilerplate'

pkgname='ros-lunar-ros-control-boilerplate'
pkgver='0.4.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('gflags'
'ros-lunar-actionlib'
'ros-lunar-catkin'
'ros-lunar-cmake-modules'
'ros-lunar-control-msgs'
'ros-lunar-control-toolbox'
'ros-lunar-controller-manager'
'ros-lunar-hardware-interface'
'ros-lunar-joint-limits-interface'
'ros-lunar-roscpp'
'ros-lunar-rosparam-shortcuts'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-trajectory-msgs'
'ros-lunar-transmission-interface'
'ros-lunar-urdf'
)

depends=('ros-lunar-actionlib'
'ros-lunar-control-msgs'
'ros-lunar-control-toolbox'
'ros-lunar-controller-manager'
'ros-lunar-hardware-interface'
'ros-lunar-joint-limits-interface'
'ros-lunar-roscpp'
'ros-lunar-rosparam-shortcuts'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-trajectory-msgs'
'ros-lunar-transmission-interface'
'ros-lunar-urdf'
)

conflicts=()
replaces=()

_dir=ros_control_boilerplate
source=()
md5sums=()

prepare() {
    cp -R $startdir/ros_control_boilerplate $srcdir/ros_control_boilerplate
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

