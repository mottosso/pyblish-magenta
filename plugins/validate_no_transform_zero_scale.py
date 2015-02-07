import pyblish.api
from maya import cmds


class ValidateNoTransformZeroScale(pyblish.api.Validator):
    """ Validate there are no transforms with zero scale.
        Especially in modeling that would be a rather useless transform. :)

        .. note:
            Consider this more of a validation example, because most pipelines will check for frozen transforms
            anyway which will also take care of validating a zero scale case. Nevertheless since object's can
            hardly be found in the viewport when they would have zero scale this is a good example for automated
            validation.
    """
    # TODO: Check if this suffer from floating point precision errors. If so we need to implement a set tolerance.

    families = ['modeling']
    hosts = ['maya']
    category = 'geometry'
    version = (0, 1, 0)

    def process_instance(self, instance):
        """Process all the nodes in the instance 'objectSet' """
        member_nodes = cmds.sets(instance.name, q=1)
        transforms = cmds.ls(member_nodes, type='transform')

        invalid = []
        for transform in transforms:
            scale = cmds.xform(transform, q=1, scale=True, objectSpace=True)
            if scale == [0.0, 0.0, 0.0]:
                invalid.append(transform)

        if invalid:
            raise ValueError("Nodes found with unfrozen transforms: {0}".format(invalid))